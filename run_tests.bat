@echo off

REM Очистка предыдущих результатов
if exist htmlcov rmdir /s /q htmlcov
if exist coverage.xml del coverage.xml
if exist .coverage del .coverage

echo Запуск тестов с измерением покрытия кода...
echo =============================================

REM Запуск тестов с coverage
coverage run -m unittest discover ./project_code/tests

echo.
echo =============================================
echo Отчет о покрытии кода:
echo =============================================

REM Вывод отчета в консоль
coverage report


echo.
echo =============================================
echo Генерация вторичных отчётов:
echo =============================================

REM Генерация HTML отчета
coverage html
