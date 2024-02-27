class TextProcessor:


    def get_input(self , path , numOfResponses):

        #User input.txt
        with open(path , 'r') as f :
            data = f.readlines()
        numOfRows =  len(data)

        template = 'Generate json without ```json``` headings which stores _ responses for google forms which has ^ questions:'

        template = template.replace('^' , str(numOfRows))
        template = template.replace('_' , str(numOfResponses))

        with open(path , 'r') as f :
            data = f.read()

        final = template + "\n" + data

        return final

