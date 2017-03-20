%% compute the “Schrenk Approximation”


%% 
% some requirements and bounds for ALM on LES-type grids
% 
% relative grid spacing is approximately limited between
% dx/R between 1/30 and 1/60 (30 to 60 mesh cells per blade)
% and uniform along the actuator line
% 
% relative spacing between actuator points satisfies db/R <= 1/20
% such that rotor thrust and power are computed accurately 
% via integration over the actuator points along blade
% 
% hypothesis (for rectangular planform) that epsilon/chord = constant 
% criteria is equivalent to grid-based epsilon/dx = constant
% 
% 
% 
% db is the blade element spacing
% dx is the mesh spacing
% R  is the blade radius

%% blade geometry for the UW model 6 lab scale turbine
% radius
R    = 0.225;
Rhub = 0.0508;
r = [0.0529
    0.0587
    0.0646
    0.0704
    0.0762
    0.0821
    0.0879
    0.0938
    0.0996
    0.1054
    0.1112
    0.1171
    0.1229
    0.1287
    0.1346
    0.1404
    0.1462
    0.1521
    0.1579
    0.1638
    0.1696
    0.1754
    0.1812
    0.1871
    0.1929
    0.1987
    0.2046
    0.2104
    0.2163
    0.2221];
% chord
c = [0.0521
    0.0483
    0.0452
    0.0425
    0.0401
    0.0379
    0.0360
    0.0343
    0.0327
    0.0313
    0.0300
    0.0288
    0.0278
    0.0268
    0.0260
    0.0252
    0.0246
    0.0240
    0.0234
    0.0230
    0.0226
    0.0223
    0.0220
    0.0218
    0.0216
    0.0215
    0.0214
    0.0214
    0.0214
    0.0214];
% twist
t = [19.415
15.804
13.374
11.582
10.203
9.113
8.221
7.486
6.874
6.361
5.927
5.558
5.241
4.967
4.729
4.525
4.346
4.187
4.042
3.913
3.795
3.685
3.580
3.481
3.384
3.287
3.191
3.092
2.993
2.887];

%% re-interpolate the blade geometry to a different grid
Nb = 30; 
rr = linspace(Rhub, R, Nb+1)';
db = mean(diff(rr));
rr = linspace(Rhub+db/2, R-db/2, Nb)';
cc = interp1(r,c,rr,'pchip');
tt = interp1(r,t,rr,'pchip');


figure
hold on
plot(r,c,'o-r')
plot(rr,cc,'x-k')
legend('original','interpolated')

% 3 files to change in SOWFA after changing blade geometry
% turbineProperties, AeroDyn.ipt, turbineArrayPropertiesFAST

%% (1) 
r = rr;
c = cc;


% shift by the hub radius, so r=0 is the hub
r = r - Rhub;
R = R - Rhub;


r_star = linspace(0, R, Nb)';
c_star = interp1(r,c,r_star,'pchip');

% anything inside the hub, overwrite to hub chord
% i_hub         = r_star <= Rhub;
% c_star(i_hub) = c_star( find(i_hub,1,'last') );

% shift the radius coordinate between +/- Radius/2
c_wing = [flipud(c_star); c_star];
r_wing = linspace(-R/2, R/2, numel(c_wing))';



%% (2)

% aspect ratio (use the original chord AR)
AR = R / mean(c);

% equivalent elliptic planform with same AR
co  = mean(c) * 4/pi;
c_e = co .* sqrt(1 - (2*r_wing/R).^2);



%% (3)



%% (3a)
% n_min and n_max are dimensionaless parameters to define the
% min and max spreading width, epsilon, for a given mesh spacing, dx
n_min = 1;
n_max = 3;


% note, can choose db slightly larger than minimum mesh size, dx,
% so that grid can distinguish between adjacent actuator points


dx = 0.025;
% dx = 0.01250;
% dx = 0.01000;
% dx = 0.00750;
% dx = 0.00680;
% epsilon_Rby2 = n_min * dx;
% epsilon_o    = n_max * dx;

epsilon = max(n_max*dx*sqrt(1 - (2*r_wing/R).^2), n_min*dx);




epsilon_by_cstar = 0.25*n_max*(dx/R)*pi*AR;
% eps = epsilon_by_cstar .* c_e;

figure
hold on
plot(r_wing, epsilon, 'o-k')
% plot(r_wing, eps, 's-g')


%% 


% limit_dxR = 1/30; % ratio of dx / R (safe between 1/30 and 1/60)
% if dx/R > limit_dxR
%     error('warning, decrease dx/R ratio')
% end
% limit_dbx = 1.5; % ratio of db / dx (safe if greater than ~ 1.5)
% if db/dx < limit_dbx
%     error('warning, increase db/dx ratio')
% end



%% plot and compare the planforms

% shift radial coordinate
r_e = r_wing + R/2 + Rhub;
r = r + Rhub;
R = R + Rhub;

pit_axis = 0.25; % pitch axis
cle     = c .* pit_axis;
cte     = c.* (pit_axis - 1);
c_le     = c_star .* pit_axis;
c_te     = c_star .* (pit_axis - 1);

c_wing_le = c_wing .* pit_axis;
c_wing_te = c_wing .* (pit_axis - 1);

c_e_le = c_e .* pit_axis;
c_e_te = c_e .* (pit_axis - 1);

figure
hold on
% plot(r_star, c_le, 'o-r')
% plot(r_star, c_te, 'x-r')
% plot([r_star flipud(r_star)], [c_le flipud(c_te)], 'o-r')
plot([r flipud(r)], [cle flipud(cte)], 's-r')
% plot([r_star flipud(r_star)], [c_le flipud(c_te)], 'x-b')
plot([r_e flipud(r_e)], [c_e_le flipud(c_e_te)], 'o-k')
% plot(r_star, c_te, 'x-r')
% plot(r_wing, c_wing_le, 'o-k')
% plot(r_wing, c_wing_te, 'x-k')
% plot(r_e, c_e_le, 'o-b')
% plot(r_e, c_e_te, 'x-b')
legend('original planform','elliptic planform')
axis equal
box on; grid on;
xlim([0 R])





