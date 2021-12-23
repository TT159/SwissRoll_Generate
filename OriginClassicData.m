
    clc;
    clear all;
    close all;
    set (0,'defaultfigurecolor','w');
    
    N=1000;% # of data
    %Gaussian noise
    noise = 0.001*randn(1,N);
    %standard swiss roll data
    tt = (3*pi/2)*(1+2*rand(1,N));   
    height = 21*rand(1,N);
    X = [(tt+ noise).*cos(tt); height; (tt+ noise).*sin(tt)];% 3X1000 matrix
 

    %% Visualize the data, show the picture
    point_size = 20;
    figure(1)
    scatter3(X(1,:),X(2,:),X(3,:), point_size,tt,'filled');
    view([12 12]); 
    title("Original swiss roll");
    
    