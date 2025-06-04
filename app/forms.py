from wtforms import Form, StringField, SubmitField, validators

class ProductForm(Form):
    product_id = StringField("Kod produktu", 
        name='product_id', 
        id='product_id',
        validators=[validators.DataRequired(message="Kod produktu jesy wymagany"),
                    validators.Regexp('^[0-9]*$', message='Kod produktu moze zawierać jedynie cyfry'),
                    validators.Length(min=5, max=10, message='kod produktu')
                        
                    ]
            
        )
    submit = SubmitField("Pobierz opinie")