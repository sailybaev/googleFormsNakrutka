from AI import GenResponses
from AI import TextProcessor


gen = GenResponses.GenResponses()
tt = TextProcessor.TextProcessor()
query = tt.get_input("/Users/sailybaev/PycharmProjects/googleFormsNakrutka/AI/user_input.txt" , 10)
gen.genResp(query , '/Users/sailybaev/PycharmProjects/googleFormsNakrutka/tempFiles/aiGeneratedJson.json')
