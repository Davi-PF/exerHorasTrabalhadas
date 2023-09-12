import unittest
from horas_trabalhadas import HorasTrabalhadas

class TestHorasTrabalhadas(unittest.TestCase):
    def test_calcular_horas_trabalhadas_com_intervalo(self):
        self.assertEqual(HorasTrabalhadas.calcular_horas_trabalhadas("09:00", "17:00", "01:00"), 7.0)
        self.assertEqual(HorasTrabalhadas.calcular_horas_trabalhadas("0830", "1200", "0030"), 3.0)

    def test_calcular_horas_trabalhadas_com_intervalo_hora_invalida(self):
        with self.assertRaises(ValueError):
            HorasTrabalhadas.calcular_horas_trabalhadas("17:00", "09:00", "01:00") # Hora de término anterior à hora de início

    def test_calcular_horas_trabalhadas_com_intervalo_duracao_invalida(self):
        with self.assertRaises(ValueError):
            HorasTrabalhadas.calcular_horas_trabalhadas("09:00", "17:00", "2400") # Duração de intervalo inválida

    def test_calcular_horas_trabalhadas_com_intervalo_invertido(self):
        self.assertEqual(HorasTrabalhadas.calcular_horas_trabalhadas("17:00", "09:00", "01:00"), 7.0)

    def test_validar_formato_hora(self):
        self.assertTrue(HorasTrabalhadas.validar_formato_hora("09:00"))
        self.assertTrue(HorasTrabalhadas.validar_formato_hora("1230"))
        self.assertFalse(HorasTrabalhadas.validar_formato_hora("9:00")) # Formato inválido (faltando zero à esquerda)
        self.assertFalse(HorasTrabalhadas.validar_formato_hora("960"))  # Formato inválido (faltando "H" ou "HH")
        self.assertFalse(HorasTrabalhadas.validar_formato_hora("12345")) # Formato inválido (mais de 4 dígitos)

if __name__ == '__main__':
    unittest.main()
