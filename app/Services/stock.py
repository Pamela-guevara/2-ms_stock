from app import cache
from app.Models.stock import Stock
from app.Repositories.stock import StockRepository
from .format_logs import format_logs
from dataclasses import dataclass

logging = format_logs('StockServices')

@dataclass
class StockServices():
    repository = StockRepository()

    def update_stock(self, id_stock:int, args:dict) -> Stock:
        stock = self.repository.find_by_id(id_stock)
        if stock:
            for key, value in args.items():
                setattr(stock, key, value) if hasattr(stock, key) else logging.warning("Unknown attr in add_stock")
                
            cache.set(f'stock_{id_stock}', stock, timeout=60)
            logging.info(f'stock_{stock.id_stock} added to cache')
            return self.repository.update_stock(stock)
        logging.error("Unknown stock to update")
        return stock

    
    def find_by_id(self, id_stock: int) -> Stock:
        stock = cache.get(f'stock_{id_stock}')
        if stock is None:
            stock = self.repository.find_by_id(id_stock)
            cache.set(f'stock_{id_stock}', stock, timeout=60)
            logging.info(f'stock_{stock.id_stock} added to cache')

        logging.info(f'stock_{stock.id_stock} retrieved to cache')    
        return stock
    # El siguiente método traerá el stock que esté relacionado con un product_id
    def find_by_product_id(self, id_product: int) -> Stock:
        stock = cache.get(f'stock_product_id_{id_product}')
        if stock is None:
            stock = self.repository.find_by_product_id(id_product)
            cache.set(f'stock_product_id_{id_product}', stock, timeout=10)
            logging.info(f'stock_product_id_{id_product} added to cache')
        logging.info(f'stock_product_id_{id_product} retrieved to cache')    
        return stock