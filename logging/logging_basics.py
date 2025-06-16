# https://docs.python.org/3/howto/logging.html#basic-logging-tutorial
# https://www.youtube.com/watch?v=pxuXaaT1u3k

import logging

def main():

    logging.basicConfig(filename='logging_basics.log',  # Instead of printing the log messages, 
                                                        # the messages are sent to a file
                        
                        filemode='w',                   # default is 'a' (open for writing, appending to the end of file if it exists)
                                                        # 'w' overwrites the previous messages

                        level=logging.WARNING,          # the lowest level that is logged
                                                        # Here, only WARNING and higher level messages
                                                        # i.e. ERROR and CRITICAL will be logged

                        format='%(asctime)s %(name)s %(levelname)s %(message)s', # LogRecord attributes
                                                                                 # https://docs.python.org/3/library/logging.html#logrecord-attributes      
                                                                                 # default format is levelname:name:message
                            
                        ) 
                                                                         
    logging.debug('This is a debug message')
    logging.info('This is a info message')
    logging.warning('This is a warning message')
    logging.error('This is a error message')
    logging.critical('This is a critical message')

if __name__ == "__main__":
    main()