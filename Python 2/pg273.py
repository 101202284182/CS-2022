# TASK 1
# def playTennis(outlook, humidity, wind): 
#     if outlook == "Overcast": 
#         return "Yes" 
#     elif outlook == "Sunny": 
#         if humidity == "High": 
#             return "No" 
#         else: 
#             return "Yes"
#     else: 
#         if wind == "Strong": 
#             return "No" 
#         else: 
#             return "Yes"

# def unitTest():
#     settings = ["Overcast", "Sunny", "Low", "High", "Weak", "Strong"]
#     expected = ["Yes", "No", "Yes", "No", "Yes", "No"]

#     for i in range(0, len(settings), 3):
#         outlook, humidity, wind = settings[i], settings[i+1], settings[i+2]
#         result = playTennis(outlook, humidity, wind)
#         expected_result = expected[i//3]
#         if(result != expected_result):
#             print("Test case %d failed. Expected: %s, got: %s" % (i//3+1, expected_result, result))
#     print("All test passed.")

# unitTest()

# TASK 2
# def mechFunc(doesItMove, shouldIt):
#     if(doesItMove == True):
#         if(shouldIt == False):
#             return "Apply duct tape."
#         else:
#             return "No problem."
#     else:
#         if(shouldIt == False):
#             return "No problem."
#         else:
#             return "Apply WD-40"

# TASK 3
def fruitClassification(size, color, taste, shape):
    size, color, taste, shape = size.lower(), color.lower(), taste.lower(), shape.lower()
    if(color == "green"):
        if(size == "big"):
            return "Watermellon"
        else:
            if(size == "medium"):
                return "Grapefruit"
            else:
                return "Lemon"
    else:
        if(color == "yellow"):
            if(shape == "round"):
                if(size == "big"):
                    return "Grapefruit"
                else:
                    return "Lemon"
            else:
                return "Banana"
        else:
            if(size == "small"):
                if(taste == "sweet"):
                    return "Cherry"
                else:
                    return "Grape"
                
            else:
                return "Apple"
            
