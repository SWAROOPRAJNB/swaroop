import logging
 
logging.basicConfig(filename='logs/app.log', level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
 
logging.info("This is an info message")
logging.warning("This is a warning message")
logging.error("this is an error message")
print("logging completed successfully")
 