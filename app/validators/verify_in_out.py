from functools import wraps
from flask import jsonify

def verify_in_out(func):
    @wraps(func)
    def decorated_verify_func(stock_data, *args, **kwargs):
        in_out_value = stock_data.get('in_out')  # Busca la clave 'in_out' en el objeto dict
        if in_out_value not in (1, 2):
            return jsonify({'error': " 'in_out' values must been 1 for (IN) or 2 for (OUT)"}), 400
        
        return func(stock_data, *args, **kwargs)  # Llama a la función original
    
    return decorated_verify_func
