from random import randint
from cpf_uteis import *


def etapa1_dv1(cpf):
    return sum(((i + 2) * int(d) for i, d in enumerate(cpf[::-1])))


def etapa1_dv2(cpf):
    return sum(((i + 3) * int(d) for i, d in enumerate(cpf[::-1])))


def etapa2_dv1(cpf):
    resultado = etapa1_dv1(cpf) * 10 % 11 
    return resultado if resultado < 10 else 0


def etapa2_dv2(cpf):
    resultado = (etapa1_dv2(cpf) + etapa2_dv1(cpf) * 2) * 10 % 11
    return resultado if resultado < 10 else 0


def filtra_mascara_cpf(cpf):
    return "".join([num for num in cpf if num.isdigit()])
    

def dv(cpf):
    cpf = filtra_mascara_cpf(cpf)
    return str(etapa2_dv1(cpf)) + str(etapa2_dv2(cpf))


def verifica_tem_11_numeros(cpf):
    cpf = filtra_mascara_cpf(cpf)
    return len(cpf) == 11


def verifica_sequencia_cpf(cpf):
    cpf = filtra_mascara_cpf(cpf)
    return (cpf[0] * len(cpf)) == cpf


def validador_cpf(cpf):
    cpf_filtrado = filtra_mascara_cpf(cpf)
    if verifica_tem_11_numeros(cpf_filtrado) and not verifica_sequencia_cpf(cpf_filtrado) and dv(cpf_filtrado[0:9]) == cpf_filtrado[-2:]:
        return True
    return False


def gera_cpf_com_mascara():
    cpf = "".join([str(randint(0,9)) for _ in range(0,9)])

    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{dv(cpf)}"


def gera_cpf_sem_mascara():
    cpf = "".join([str(randint(0,9)) for _ in range(0,9)])

    return cpf + dv(cpf)