import get_coefficients # fonction entire_regression


def ask(source,degree):

    coefs = get_coefficients.entire_regression(source,degree)

    response = input("\nChange initial coefficients of movement ? (yes:1 / no:2) : ")
    if(response == 1):
        for i in range(1,13):
            question = "Change motor" + str(i) +" ? (yes:1 / no:2) : "
            response = input(question)
    else:
        print coefs
    










    
ask("screenlog_interpolation.txt", 10)
    
