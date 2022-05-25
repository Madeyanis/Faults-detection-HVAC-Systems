clear all
close all
clc


data = readtable('C:\Users\masdoua1\OneDrive\Research\DataBase\MZVAV-1.csv');

%% Day 1
day1 = data(1:(1439+35*1440), 2:end);
day1 = table2array(day1);
AHU_ReturnAirTemp = day1(:, 5); AHU_ReturnAirTemp_C = (AHU_ReturnAirTemp -32)*(5/9); % Fahrenheit and celsius
AHU_SupplyAirTemp = day1(:, 1); AHU_SupplyAirTemp_C = (AHU_SupplyAirTemp -32)*(5/9); % Fahrenheit and celsius 
AHU_SupplyAirTempSetPoint = day1(:, 2); AHU_SupplyAirTempSetPoint_C = (AHU_SupplyAirTempSetPoint -32)*(5/9); % Fahrenheit and celsius 
AHU_OutDoorAirTemp = day1(:, 3); AHU_OutDoorAirTemp_C = (AHU_OutDoorAirTemp -32)*(5/9); % Fahrenheit and celsius 

%% Plot day1

figure(1) % Fahrenheit
plot(AHU_ReturnAirTemp_C)
hold on 
plot(AHU_SupplyAirTemp_C)
hold on 
plot(AHU_SupplyAirTempSetPoint_C)
hold on
plot(AHU_OutDoorAirTemp_C)
legend('Return Air', 'Supp Air', 'Supp Air SetPoint', 'Out Door Air')

figure(2); % Celsius
plot(AHU_ReturnAirTemp)
hold on 
plot(AHU_SupplyAirTemp)
hold on 
plot(AHU_SupplyAirTempSetPoint)
hold on
plot(AHU_OutDoorAirTemp)
legend('Return Air', 'Supp Air', 'Supp Air SetPoint', 'Out Door Air')


%%
Data2 = readtable('C:\Users\masdoua1\OneDrive\Research\DataBase\MZVAV-2-1.csv');
%% Day 1
day = Data2(1:1439, 2:end);
day = table2array(day);
AHU_ReturnAirTemp = day(:, 5); AHU_ReturnAirTemp_C = (AHU_ReturnAirTemp -32)*(5/9); % Fahrenheit and celsius
AHU_SupplyAirTemp = day(:, 1); AHU_SupplyAirTemp_C = (AHU_SupplyAirTemp -32)*(5/9); % Fahrenheit and celsius 
AHU_SupplyAirTempSetPoint = day(:, 2); AHU_SupplyAirTempSetPoint_C = (AHU_SupplyAirTempSetPoint -32)*(5/9); % Fahrenheit and celsius 
AHU_OutDoorAirTemp = day(:, 3); AHU_OutDoorAirTemp_C = (AHU_OutDoorAirTemp -32)*(5/9); % Fahrenheit and celsius 

%% Plot day1

figure(3) % Fahrenheit
plot(AHU_ReturnAirTemp_C)
hold on 
plot(AHU_SupplyAirTemp_C)
hold on 
plot(AHU_SupplyAirTempSetPoint_C)
hold on
plot(AHU_OutDoorAirTemp_C)
legend('Return Air', 'Supp Air', 'Supp Air SetPoint', 'Out Door Air')

figure(4); % Celsius
plot(AHU_ReturnAirTemp)
hold on 
plot(AHU_SupplyAirTemp)
hold on 
plot(AHU_SupplyAirTempSetPoint)
hold on
plot(AHU_OutDoorAirTemp)
legend('Return Air', 'Supp Air', 'Supp Air SetPoint', 'Out Door Air')