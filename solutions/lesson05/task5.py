def reg_validator(reg_expr: str, text: str) -> bool:  
    if not reg_expr and not text:
        return True
    if not reg_expr or not text:
        return False
    ind_text = 0
    digit = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for j in range(len(reg_expr)):
    
        if ind_text>=len(text) and j < len(reg_expr):
            return False
        if  ind_text>=len(text):
            break
                
        elif reg_expr[j] == "d":
            if not text[ind_text].isdigit():
                return False
            while text[ind_text].isdigit():
                ind_text+=1
                
                if ind_text>=len(text):
                    break
                
        elif reg_expr[j] == "w":
            if text[ind_text].isdigit():
                return False
            while text[ind_text] in digit:
                ind_text+=1
                if ind_text>=len(text):
                    break
                
        elif reg_expr[j] == "s":
            if not text[ind_text].isdigit() and (not text[ind_text] in digit):
                return False
            while text[ind_text] in digit or text[ind_text].isdigit():
                ind_text+=1
                if ind_text>=len(text):
                    break
                
        elif  reg_expr[j] == text[ind_text]:
            ind_text +=1
        else:
            return False
    return True 
