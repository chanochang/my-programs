function []= planarArm()

clc
clear all;
close all;
%parameters for the arm
I1=0.1213;  I2 = 0.0116; m1=6.5225; r1=0.098; m2=2.0458; r2=0.0229; l1=0.26; l2=0.26; g = 9.8;


% we compute the parameters in the dynamic model
a = I1+I2+m1*r1^2+ m2*(l1^2+ r2^2);
b = m2*l1*r2;
d = I2+ m2*r2^2;

%%

% initial condition - Format:[theta1,theta2,dtheta1,dtheta2]
x0= [0,0,0,0]; %You can change the initial condition here.

tf=10;

% the options for ode - Optional!
%options = odeset('RelTol',1e-4,'AbsTol',[1e-4, 1e-4, 1e-4, 1e-4]);

global torque allq_error
torque=[];
allq_error = []; 


%% Implement the PD control plus Feedforward.
index=2;
[T,X] = ode45(@(t,x)plannarArmODE(t,x,index),[0 tf],x0);


fig =  figure('Name','Graphs of position errors ˜q1 and ˜q2');
plot(T, allq_error(1,1:size(T,1)), 'r-');
hold on
plot(T, allq_error(2,1:size(T,1)), 'b-');  xlim([0, 15]);
%print(fig,'Prob3_Output','-dpng')

%% Functions

    function [dx ] = plannarArmODE(t,x,idx)
        b1 = 3.14/4; c1 = 3.14/9; w1 = 4; b2 = 3.14/3; c2 = 3.14/6; w2 = 3; 
        theta_d= [(b1*(1 - exp(-2.0 * t^3))) + (c1*(1 - exp(-2.0 * t^3))* sin(w1 * t));
                (b2*(1 - exp(-2.0 * t^3))) + (c2*(1 - exp(-2.0 * t^3))* sin(w2 * t))]; %You can insert any desired joint trajectory here!
        dtheta_d =[(6 * b1 * t^2 * exp(-2.0* t^3)) + ((6 * c1 * t^2 * exp(-2.0* t^3)) * sin(w1 * t)) + ((c1 - (c1* exp(-2.0* t^3))) * (cos(w1*t))*w1);
            (6 * b2 * t^2 * exp(-2.0* t^3)) + ((6 * c2 * t^2 * exp(-2.0* t^3)) * sin(w2 * t)) + ((c2 - (c2* exp(-2.0* t^3))) * (cos(w2*t))*w2)]; %Time derivative of theta_d
        ddt1d = (12 * b1 * t* exp(-2.0* t^3)) - (36*b1*t^4 * exp(-2.0* t^3)) + (12* c1 * t * (exp(-2.0* t^3))* sin(w1 * t)) -  ((36*c1*t^4 * exp(-2.0* t^3)) * sin(w1 * t)) +(12* c1 * t^2 * (exp(-2.0* t^3))* (cos(w1 * t)) * w1) - (c1 - (c1 * (exp(-2.0* t^3))) * (sin(w1 * t))* w1^2);
        ddt2d = (12 * b2 * t* exp(-2.0* t^3)) - (36*b2*t^4 * exp(-2.0* t^3)) + (12* c2 * t * (exp(-2.0* t^3))* sin(w2 * t)) -  ((36*c2*t^4 * exp(-2.0* t^3)) * sin(w2 * t)) +(12* c2 * t^2 * (exp(-2.0* t^3))* (cos(w2 * t)) * w2) - (c2 - (c2 * (exp(-2.0* t^3))) * (sin(w2 * t))* w2^2);
        ddtheta_d = [ddt1d ; ddt2d]; %Second time derivated of theta_d
        theta= x(1:2,1);
        dtheta= x(3:4,1);
        q_error = [theta_d(1) - x(1,1); theta_d(2) - x(2,1)]; 
        allq_error = [allq_error q_error];

        global Mmat Cmat Mmatd Cmatd Gmat
        Mmat = [a+2*b*cos(x(2)), d+b*cos(x(2));  d+b*cos(x(2)), d];
        Cmat = [-b*sin(x(2))*x(4), -b*sin(x(2))*(x(3)+x(4)); b*sin(x(2))*x(3),0];
        Gmat = [ (((m1*r1 + m2*l1) * g * sin(x(1))) +  ( m2*r2 * g * sin(x(1)+x(2)))  ); m2*r2 * g * sin(x(1)+x(2))];
        Mmatd = [a+2*b*cos(theta_d(2)), d+b*cos(theta_d(2));  d+b*cos(theta_d(2)), d];
        Cmatd = [-b*sin(theta_d(2))*dtheta_d(2), -b*sin(theta_d(2))*(dtheta_d(1)+dtheta_d(2)); b*sin(theta_d(2))*dtheta_d(1),0];
        invM = inv(Mmat);
        invMC = invM*Cmat;
        switch idx 
            case 1
                tau = computeTorque(theta_d, dtheta_d, ddtheta_d, theta, dtheta); %
            
            case 2
                tau = PDplusFeedforwawrd(theta_d, dtheta_d, ddtheta_d, theta, dtheta);
        end
        torque =[torque, tau];


        dx=zeros(4,1);
        dx(1) = x(3);
        dx(2) = x(4);
        dx(3:4) = -invMC* x(3:4) +invM*tau; % because ddot theta = -M^{-1}(C \dot Theta) + M^{-1} tau
    end

  

    function tau = PDplusFeedforwawrd(theta_d, dtheta_d,ddtheta_d, theta, dtheta)
        global Mmatd Cmatd
        Kp=[200 ,0 ; 0 , 150];
        Kv=[3 ,0 ; 0 , 3];
        e=theta_d-theta; % position error
        de = dtheta_d - dtheta; % velocity error
        tau= (Kp*e + Kv*de) + Cmatd*dtheta_d + Mmatd*ddtheta_d;
    end
disp('Finish.');

end
