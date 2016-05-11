class CPF(object):
    @classmethod
    def validate(cls, cpf):
        """
        Valida o CPF recebido
            @param cpf: string - CPF a ser validado
            @return: bool - se o CPF é válido ou não
        """

        if not cpf:
            return False

        # obtém os digitos do CPF (apenas os numeros)
        cpf_digitos = "".join([d for d in str(cpf) if d.isdigit()])

        # deve haver 11 digitos
        if len(cpf_digitos) != 11:
            return False

        cpf_invalidos = [11 * str(i) for i in range(10)]

        # não pode ser um número com todos os
        # digitos iguais, ex: 11111111111, 222222222, 33333333, etc
        if cpf_digitos in cpf_invalidos:
            return False

        # transforma a string em uma lista
        cpf_lista = [str(x) for x in cpf]

        if cpf_lista[3] != '.' or cpf_lista[7] != '.' or cpf_lista[11] != '-':
            return False

        return True

class CEP(object):
    @classmethod
    def validate(cls, cep):
        """
        Valida o CPF recebido
            @param cpf: string - CPF a ser validado
            @return: bool - se o CPF é válido ou não
        """

        if not cep:
            return False

        cep_digitos = "".join([d for d in str(cep) if d.isdigit()])

        # deve haver 8 digitos
        if len(cep_digitos) != 8:
            return False

        cep_invalidos = [11 * str(i) for i in range(10)]

        # não pode ser um número com todos os
        # digitos iguais, ex: 11111111111, 222222222, 33333333, etc
        if cep_digitos in cep_invalidos:
            return False

        # transforma a string em uma lista
        cep_lista = [str(x) for x in cep]

        if cep_lista[5] != '-':
            return False

        return True