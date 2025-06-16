# https://docs.python.org/3/howto/logging.html#advanced-logging-tutorial

import logging

'''
logging library offers several components: loggers, handlers, filters, and formatters.

    - Loggers expose the interface that application code directly uses. The root of the hierarchy of loggers 
      is called the root logger.

    - Handlers send the log records (created by loggers) to the appropriate destination such as files, 
      HTTP GET/POST locations, email via SMTP, generic sockets, queues, or OS-specific logging mechanisms 
      such as syslog or the Windows NT event log.

    - Filters provide a finer grained facility for determining which log records to output.

    - Formatters specify the layout of log records in the final output.

'''
def main():

    logger = logging.getLogger(__name__) # __name__ is set to the name of the module
    
    logger.debug('This is a debug message')
    logger.info('This is a info message')
    logger.warning('This is a warning message')
    logger.error('This is a error message')
    logger.critical('This is a critical message')

if __name__ == "__main__":
    main()