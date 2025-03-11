from app import db
from sqlalchemy.exc import IntegrityError, NoResultFound
from app.Models.stock import Stock
from app.Services.format_logs import format_logs

logging = format_logs('StockRepository')

class StockRepository:

    def update_stock(self, stock: Stock) -> Stock:
        try:
            db.session.add(stock)
            db.session.commit()
            logging.info(f'Stock {stock.id_stock} updated successfully')
            return stock
        except IntegrityError as e:
            db.session.rollback()
            logging.error(f'Stock {stock.id_stock} cannot update, error {e}')
            raise e        
            
    def find_by_id(self, id: int) -> Stock :
        try:
            res = db.session.query(Stock).filter(Stock.id_stock == id).one()
            logging.info(f'Stock with id {id} found successfully')
            return res
        except NoResultFound as e:
            logging.error(f'Stock id {id} not found, error {e}')
            raise e
        
    def find_by_product_id(self, id_product: int) -> Stock:
        try:
            res = db.session.query(Stock).filter(Stock.id_product == id_product).one_or_none()
            logging.info(f'Stock where id_product {id} found succefully')
            return res
        except NoResultFound as e:
            logging.info(f'Stocks where id_product {id} not found, error {e}')
            raise e