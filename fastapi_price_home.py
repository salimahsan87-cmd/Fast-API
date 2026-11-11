
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Literal, Optional

from tensorflow.keras.models import load_model
import pandas as pd
import numpy as np
import joblib


model = load_model('price_home_canada.h5', compile=False)

pipe = joblib.load('preprocessing2.joblib')

encoder = pipe['encoder']
standard = pipe['scaler_x']
standard_y = pipe['scaler_y']

column_stand = pipe['x_stand']


app = FastAPI(title='Price Home Canada')


class PriceHome(BaseModel):

    property_type: Literal['SFD', 'SFA', 'TH', 'Apart']

    Location: str = Field(min_length=1)

    CompIndex: float = Field(gt=0)
    CompYoYChange: float

    year: int = Field(ge=2015, le=2021)

    
    SFDetachIndex: Optional[float] = None
    SFDetachBenchmark: Optional[float] = None
    SFDetachYoYChange: Optional[float] = None

    
    SFAttachIndex: Optional[float] = None
    SFAttachBenchmark: Optional[float] = None
    SFAttachYoYChange: Optional[float] = None

    
    THouseIndex: Optional[float] = None
    THouseBenchmark: Optional[float] = None
    THouseYoYChange: Optional[float] = None

    
    ApartIndex: Optional[float] = None
    ApartBenchmark: Optional[float] = None
    ApartYoYChange: Optional[float] = None



property_columns = {
    'SFD': [
        'SFDetachIndex',
        'SFDetachBenchmark',
        'SFDetachYoYChange'
    ],

    'SFA': [
        'SFAttachIndex',
        'SFAttachBenchmark',
        'SFAttachYoYChange'
    ],

    'TH': [
        'THouseIndex',
        'THouseBenchmark',
        'THouseYoYChange'
    ],

    'Apart': [
        'ApartIndex',
        'ApartBenchmark',
        'ApartYoYChange'
    ]
}


missing_columns = [
    'SFAttachIndex_missing',
    'SFAttachBenchmark_missing',
    'SFAttachYoYChange_missing',

    'THouseIndex_missing',
    'THouseBenchmark_missing',
    'THouseYoYChange_missing',

    'ApartIndex_missing',
    'ApartBenchmark_missing',
    'ApartYoYChange_missing'
]


feature_order = [
    'Location',
    'CompIndex',
    'CompYoYChange',

    'SFDetachIndex',
    'SFDetachBenchmark',
    'SFDetachYoYChange',

    'SFAttachIndex',
    'SFAttachBenchmark',
    'SFAttachYoYChange',

    'THouseIndex',
    'THouseBenchmark',
    'THouseYoYChange',

    'ApartIndex',
    'ApartBenchmark',
    'ApartYoYChange',

    'year',

    *missing_columns
]


@app.get('/')
def message():

    return {
        'message': 'Price Home API is running'
    }


@app.post('/predict')
def predict_price_home(data: PriceHome):

    try:


        row = {
            col: 0 for col in feature_order
        }


        row['Location'] = data.Location
        row['CompIndex'] = data.CompIndex
        row['CompYoYChange'] = data.CompYoYChange
        row['year'] = data.year

        selected_columns = property_columns[data.property_type]

        for col in selected_columns:

            value = getattr(data, col)

            if value is None:
                raise HTTPException(
                    status_code=422,
                    detail=f'{col} is required for {data.property_type}'
                )

            row[col] = value


        for property_type, columns in property_columns.items():

            if property_type == 'SFD':
                continue

            for col in columns:

                indicator = col + '_missing'

                if property_type == data.property_type:
                    row[indicator] = 0
                else:
                    row[indicator] = 1


        input_data = pd.DataFrame(
            [row],
            columns=feature_order
        )


        input_data[['Location']] = encoder.transform(
            input_data[['Location']]
        )


        input_data[column_stand] = standard.transform(
            input_data[column_stand]
        )


        prediction = model.predict(
            input_data,
            verbose=0
        )


        prediction = standard_y.inverse_transform(
            prediction.reshape(-1, 1)
        )

        prediction = np.exp(prediction)

        benchmark = float(prediction[0][0])


        return {
            'property_type': data.property_type,
            'predicted_benchmark': round(benchmark, 2)
        }


    except HTTPException:
        raise

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
