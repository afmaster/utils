
def replacing(string_para_salvar):
    st = string_para_salvar.replace("é", "e")
    st = st.replace("É", "E")
    st = st.replace("é", "e")
    st = st.replace("Ã", "A")
    st = st.replace("Â", "A")
    st = st.replace("â", "a")
    st = st.replace("Á", "A")
    st = st.replace("á", "a")
    st = st.replace("ã", "a")
    st = st.replace("Õ", "O")
    st = st.replace("Ô", "O")
    st = st.replace("Ó", "O")
    st = st.replace("õ", "o")
    st = st.replace("ô", "o")
    st = st.replace("ó", "o")
    st = st.replace("ê", "e")
    st = st.replace("Ê", "E")
    st = st.replace("Í", "I")
    st = st.replace("í", "i")
    st = st.replace("ç", "c")
    st = st.replace("Ç", "C")
    return st

def ajust_to_sql(par):
    str_par = str(par)
    parsed_par = str_par.replace("'", '"')
    return parsed_par
