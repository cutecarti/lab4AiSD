# Лабораторная работа 4 Горашко А.С ИСТбд-12, 
11. Формируется матрица F следующим образом: скопировать в нее А и если в С сумма чисел  в нечетных столбцах больше, чем произведение чисел в четных строках, то поменять местами В и С симметрично, иначе Е и В поменять местами несимметрично. При этом матрица А не меняется. После чего если определитель матрицы А больше суммы диагональных элементов матрицы F,то вычисляется выражение:A-1*AT – K * F-1, иначе вычисляется выражение (AТ +G-1-F-1)*K, где G-нижняя треугольная матрица, полученная из А. Выводятся по мере формирования А, F и все матричные операции последовательно.
для тестирования можете использовать заготовленные строки чисел:
(Строка для матрицы 6х6)
6 -2 3 5 5 4 6 -7 -8 5 3 5 6 9 4 3 5 3 5 6 7 8 9 6 0 3 2 -1 -2 -6 -8 3 2 3 4 5
(Строка для матрицы 7х7)
7 9 1 7 4 -1 -8 5 3 1 -2 -1 -5 -6 -1 -5 6 9 3 -1 -4 5 -4 -5 -1 6 9 8 5 6 7 8 3 1 2 -2 -5 -1 5 -6 -7 8 5 6 3 -3 -5 -5 -6
