import view
import model

def start():
    while True:
        choice=view.main_menu()
        match choice:
            case 1:
                model.open_pb()
                view.print_message(text.load_succesful)
        match choice:    
            case 2:
                pass
        match choice:
            case 3:
                pass
        match choice:
            case 4:
                pass
        match choice:
            case 5:
                pass
        match choice:
            case 6:
                pass
        match choice:
            case 7:
                pass
        match choice:
            case 8:
                break    


        