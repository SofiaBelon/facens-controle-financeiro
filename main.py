class Initialize ():
    def __init__(self):
        self.__transactions = []

    def show_menu(self):
        
        print('Welcome to Financial Control application')
        print('1 - Add transaction')
        print('2 - Show transaction')
        print('3 - Exit')


    def choose_option(self):
        option = input('Choose one of the following options: ')
        
        if option not in ['1', '2', '3']:
            print('\nInvalid option')

        return option 

    def to_add(self):
        operation = input('Input the operation type:')
        value = input( 'Input the value: ')
        description = input('input a description: ')

        self.__transactions.append(
            (operation, value, description)
        )
    
    def to_view(self):
        for transaction in self.__transactions:
            print(f'Operation: {transaction[0]} - Value: {transaction[1]} - Description: {transaction[2]}')
            
    def to_go_out(self):
        print('\nThak you, always come back')

if __name__ == '__main__':
    init = Initialize()

    option = ''
    
    while option != '3':
        init.show_menu()
        
        option = init.choose_option()
        if option == '1':
            init.to_add()
        elif option == '2':
            init.to_view()
        elif option == '3':
            init.to_go_out()
