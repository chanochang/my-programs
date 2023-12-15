clear all
close all
clc
Control ();

%% Main function that runs everything
function Control()

%% Globals for data collection
global force
global timeStep
global torque
force = [];
timeStep =[];
torque =[];

%% ODE45 required parameters
xi = 1; yi = 0; % Starting Position
q_i = invKin(xi,yi); % Statring Theta
q_des = 135 * pi/180;
q_i_error = q_des - q_i;

X0 = [q_i_error ; 0]; % Format: [q_error; q_d]
tf = 10;

[T,X] = ode45(@(t,x)robotArm(t,x), [0 tf], X0);

%% Plot Everything
figure('Name', 'Joint Angle vs Time');
plot(T, rad2deg(q_des - X(:,1)),'LineWidth', 3);
title('Joint Angle vs time');
xlabel('Time (sec)');
ylabel('Angle (deg)');
legend('q1', 'Location', 'northwest');

figure('Name', 'Joint Velocity vs Time');
plot(T, rad2deg(X(:,2)),'LineWidth', 3);
title('Joint Velocity vs Time');
xlabel('Time (sec)');
ylabel('Velocity (deg/sec)');
legend('q1 dot', 'Location', 'northwest');

% Find EE pose and pose error
x = [];
y = [];
x_err = [];
y_err = [];
x_des = -sqrt(2)/2;
y_des = sqrt(2)/2;

for i =1:length(X)
    pos = forKin(q_des - X(i,1));
    x = [x; pos(1)];
    y = [y; pos(2)];
    x_err = [x_err; x_des - pos(1)];
    y_err = [y_err; y_des - pos(2)];
end 

figure('Name', 'EE position vs time');
plot(T, x, T, y,'LineWidth', 3);
title('EE position vs time');
xlabel('Time (sec)');
ylabel('Position (m)');
legend('x', 'y', 'Location', 'northwest'); 

figure('Name', 'EE position error vs time');
plot(T, x_err, T, y_err, 'LineWidth', 3);
title('EE position error vs time');
xlabel('Time (sec)');
ylabel('Position Error (m)');
legend('x', 'y', 'Location', 'northwest');

figure('Name', 'Control Input vs Time');
plot(timeStep, torque,'LineWidth', 3);
title('Control Input vs Time');
xlabel('Time (sec)');
ylabel('Joint Torque (Nm)');
legend('Tau', 'Location', 'northwest');

figure('Name', 'EE Force vs time');
plot(timeStep, force(:, 1), timeStep, force(:, 2), 'LineWidth', 3);
title('EE Force vs time');
xlabel('Time (sec)');
ylabel('Force (Nm)');
legend('x', 'y', 'Location', 'northwest');

figure('Name', 'Stick Plot Model');
grid on
line([-0.1,-0.1], [0.8,1.1],'LineWidth', 55, 'Color', 'black'); % Where the obstacle is
line([0,1], [0,0],'LineWidth', 3, 'Color', 'blue');  % Starting pose
line([0, x(end)], [0, y(end)],'LineWidth', 3, 'Color', 'red');  % Ending pose 
xlabel('X (meters)');
ylabel('Y (meters)');
legend('Obstacle', 'Initial Pose', 'Final Pose');
    %%

end
%% Differential Equations
function dx = robotArm(t,x)
% Controller Gains
global Kp
global Kd
global K
Kp = 0.5;
Kd = 1;
K = 10;

%% Solve for Dynamic Model
[M, C, G] = dynamicModel(x);

q_des = 135 * pi/180;
q1 = q_des - x(1);
q1_dot = x(2);

% End Position
x_des = -sqrt(2)/2;
y_des = sqrt(2)/2;

% Obstacle
xr = 0;

%Current Position
xe = forKin(q1);

% Errors
x_error = x_des - xe(1);
y_error = y_des - xe(2);
pos_errors = [x_error ; y_error];

% Force Experienced from Obstacle
he = [0 ; 0];

% Determine if hitting obstacle
if (xe(1) <= xr)
    he = [Kp*K/(Kp + K)*(x_des - xr) ; 0];
end

% Track EE fore
global force
global timeStep
force = [force ; [he(1) , he(2)]];
timeStep = [timeStep ; t];

% Jacobioan
a= 1;
J = [-a*sin(q1);a*cos(q1)];

%% Compliance Control
tau = G + transpose(J) * Kp * pos_errors - transpose(J) * Kd * J * q1_dot;

%% Track Joint Torque
global torque
torque = [torque , tau];

%% State Space Model
q_dd = inv(M) * (tau - C*q1_dot - G - transpose(J) * he);
dx = zeros (2,1);
dx(1) = -q1_dot;
dx(2) = q_dd;

end


%% Dynamic Model
function [M, C, G] = dynamicModel(x) 
m1 = 0.5;
a = 1;
g = 9.8;
q_des = 135 * pi/180;
q = q_des - x(1);
q_dot = x(2);
% Based on: m*a^2*theta_dd + m*g*a*cos(theta)

M = m1*a^2;
C = 0;
G = m1 *g*a*cos(q);

end

%% Inverse Kinematics
function q = invKin(x,y)
q = atan2(y,x);
end

%% Forward Kinematics
function pos = forKin(q)
a = 1; % Length of arm

x = a * cos(q);
y = a * sin(q);
pos = [x;y];
end