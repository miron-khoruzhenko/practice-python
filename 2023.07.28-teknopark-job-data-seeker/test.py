import sys, time
# write = sys.stdout.write

# text = 'hello'
# # for c in text:  
# #     write(c)
# #     time.sleep(.5)
# #     write('\b')

# write(text)

class DriverOptions:
    def __init__(self):
        
        self.dynamic_word_len = 0

        self.dynamic_print('hello 11')
        self.dynamic_print('hello 22')


    def dynamic_print(self, dynamic_msg):
        write = sys.stdout.write
        write('\b' * self.dynamic_word_len)

        write(dynamic_msg)
                
        self.dynamic_word_len = len(dynamic_msg) + 1
    
        write('\n')
    # write('\b' * backup_len)

if __name__ == '__main__':
    bot = DriverOptions()
    # bot.start()
