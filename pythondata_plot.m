
clear, clc, close all;
set (0,'defaultfigurecolor','w')

%load data
X = load("2Brokendata2000_iso.csv");
labels = load("2Brokenlabel2000_iso.csv");
% X = load("4Brokendata2000_iso.csv");
% labels = load("4Brokenlabel2000_iso.csv");
X = X';

% plot the 3-D scatter
point_size = 10;
figure(1)
scatter3(X(1,:),X(2,:),X(3,:), point_size,labels,'filled');
title("2 Classes Broken Swiss Roll Dataset");
view([12 12]);



