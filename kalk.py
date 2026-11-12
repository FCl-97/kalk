def base_converter(number_str, from_base, to_base):
  try:
    decimal_number = int(number_str, from_base)
  except ValueError:
    return 'Ошибка: число не соответствует исходной системе счисления.'

  if decimal_number == 0:
    return '0'

  if to_base == 10:
    return str(decimal_number)

  digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  res = []
  n = decimal_number

  while n > 0:
    res.append(digits[n % to_base])
    n //= to_base

  return ''.join(reversed(res))

if __name__ == '__main__':
  print('Калькулятор систем счисления')
  num = input('Введите число: ').strip()
  base_from = int(input('Исходная система счисления (2-36): '))
  base_to = int(input('Целевая система счисления (2-36): '))

  result = base_converter(num, base_from, base_to)
  print(f'Результат: {result}')
