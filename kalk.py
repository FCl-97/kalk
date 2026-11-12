def base_converter(number_str, from_base, to_base):

  try:
    decimal_number = int(number_str, from_base)
  except ValueError:
    return 'Ошибка: число или основание введены некорректно.'

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
  print("Для завершения работы введите 'выход' вместо числа.\n")

  while True:
    num = input('Введите число: ').strip()

    if num.lower() in ('end', 'выход', 'q'):
      print('Работа программы завершена.')
      break

    try:
      base_from = int(input('Исходная система счисления (2-36): '))
      base_to = int(input('Целевая система счисления (2-36): '))
    except ValueError:
      print('Ошибка: основание системы должно быть целым числом!\n')
      continue

    result = base_converter(num, base_from, base_to)
    print(f'Результат: {result}\n' + '-' * 35)
