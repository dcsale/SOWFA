%% preamble
clear all;
close all;
clc;

addpath([pwd filesep 'sort_nat']);

%% USER INPUTS

% directory where FAST ouput is stored
% dir_TurbineOutput = '/mnt/data-RAID-1/danny/fastFlume-Hyak-saved-runs/mesh=Coarse/Coarse-e1/turbineOutput';
% dir_TurbineOutput = '/mnt/data-RAID-1/danny/fastFlume-Hyak-saved-runs/mesh=Coarse/Coarse-e2/turbineOutput';
% dir_TurbineOutput = '/mnt/data-RAID-1/danny/fastFlume-Hyak-saved-runs/mesh=Coarse/Coarse-e3/turbineOutput';
% dir_TurbineOutput = '/mnt/data-RAID-1/danny/fastFlume-Hyak-saved-runs/mesh=Coarse/Coarse-e4/turbineOutput';
% dir_TurbineOutput = '/gscratch/stf/dsale/job_output/saved-runs-fastFlume/turbineOutput';
dir_TurbineOutput = '../../turbineOutput';

% select the turbine type (and modify corresponding flow conditions if needed)
% an improvement would be to read these variables directory from the OpenFOAM case files
% current options: 'NREL-5MW'
%                  'DOE-RM1-DualRotor'
%                  'DOE-RM1-SingleRotor'
%                  'UW-LabScale-Array'
%                  'UW-LabScale-Single'
turbineType = 'UW-LabScale-Single';
switch turbineType       
    case{'DOE-RM1'}
        % DOE RM1 full scale hydrokinetic turbine dual rotor
        U_inf    = 1.9;                                 % free stream velocity
        density  = 1025;                                % fluid density
        RotorRad = 10.0;   
        Pavail   = 0.5*density*pi*RotorRad^2*U_inf^3;   % available KE of uniform flow
        nTurbines = 2;                                  % number of turbines
        idTurbine = [0 1];                              % IDs given in SOWFA case files
        
    case{'UW-LabScale-Array'}
        % UW lab scale (rev 1) of DOE RM1 Tidal Turbine
        U_inf     = 1.1;                                % free stream velocity of flume
        density   = 1000;                               % fluid density
        RotorRad  = 0.225;                              % 45:1 scaling of geometry
        Pavail    = 0.5*density*pi*RotorRad^2*U_inf^3;  % available KE of uniform flow
        nTurbines = 3;                                  % number of turbines
        idTurbine = [0 1 2];                            % IDs given in SOWFA case files

    case{'UW-LabScale-Single'}
        % UW lab scale (rev 1) of DOE RM1 Tidal Turbine
        U_inf     = 0.9;                                % free stream velocity of flume
        density   = 1000;                               % fluid density
        RotorRad  = 0.225;                              % 45:1 scaling of geometry
        Pavail    = 0.5*density*pi*RotorRad^2*U_inf^3;  % available KE of uniform flow
        nTurbines = 1;                                  % number of turbines
        idTurbine = [0];                                % IDs given in SOWFA case files
        
    case{'NREL-5MW'}
        % NREL 5MW wind turbine
        U_inf    = 8;                                   % free stream velocity
        density  = 1.225;                               % fluid density
        RotorRad = 63;   
        Pavail   = 5296610;                             % rated mechanical power for the NREL 5MW turbine
        % Pavail   = 0.5*density*pi*RotorRad^2*U_inf^3;   % available KE of uniform flow
        nTurbines = 3;                                  % number of turbines
        idTurbine = [0 1 2];                            % IDs given in SOWFA case files
        
    otherwise
        error('unrecognized input for turbine type (nickname)')       
end

% subset of data (allows to focus on specific part of times series, e.g. to ignore transients)
perStart = 0;   % end point - fraction of time series (between 0 and 1)
% perStart = 0.2;   % end point - fraction of time series (between 0 and 1)
perEnd   = 1;   % end point - fraction of time series (between 0 and 1)

%% END USER INPUTS
%  everything below should not need to be modified, usually

% look for all the subfolders in the directory (corresponding to when 
%  SOWFA was stopped and then restarted), and then join the data
%  from each subfolder into a single time series
DIR         = dir(dir_TurbineOutput);               % structure of directory info
isub        = [DIR(:).isdir];                       % returns logical vector
nameFolders = {DIR(isub).name}';                    % names of subfolders
nameFolders(ismember(nameFolders,{'.','..'})) = []; % remove the . and .. directories

restart_folders = nameFolders;
restart_folders = sort_nat(restart_folders);

%% load the data
data_filename  = 'powerRotor';
numCols        = 4;
nHeaders       = 1;
[time, Protor] = load_FAST_scalars(dir_TurbineOutput, ...
                                   data_filename, ...
                                   numCols, ...
                                   nHeaders, ...
                                   restart_folders, ...
                                   idTurbine, ...
                                   perStart, ...
                                   perEnd);

% data_filename  = 'thrust';
% numCols        = 4;
% nHeaders       = 1;
% [time, thrust] = load_FAST_scalars(dir_TurbineOutput, ...
%                                    data_filename, ...
%                                    numCols, ...
%                                    nHeaders, ...
%                                    restart_folders, ...
%                                    idTurbine, ...
%                                    perStart, ...
%                                    perEnd);
                               
data_filename  = 'azimuth';
numCols        = 4;
nHeaders       = 1;
[time, azimuth] = load_FAST_scalars(dir_TurbineOutput, ...
                                   data_filename, ...
                                   numCols, ...
                                   nHeaders, ...
                                   restart_folders, ...
                                   idTurbine, ...
                                   perStart, ...
                                   perEnd);
                               
%% Plot the azimuth
figure('Name', 'azimuth Blade 1', ...
       'Color', 'white');

% plot(time, Protor, 'LineWidth', 2)
hold on;
plot(time, azimuth(:,1), 'o-b', 'LineWidth', 3)
% plot(time, Protor(:,2), '-k', 'LineWidth', 3)
% plot(time, Protor(:,3), '-r', 'LineWidth', 3)

% legend('turbine upstream','turbine middle','turbine downstream', ...
%        'Location','best');
   
title('azimuth', 'FontSize', 16)
xlabel('time, t (s)', 'FontSize', 16);
ylabel('azimuth (deg)', 'FontSize', 16);
   
set(gca,'FontSize', 16)
box on
grid on                               

%% Plot the power
figure('Name', 'Rotor Power', ...
       'Color', 'white');

% plot(time, Protor, 'LineWidth', 2)
hold on;
plot(time, Protor(:,1), '-b', 'LineWidth', 3)
plot(time, Protor(:,2), '-k', 'LineWidth', 3)
plot(time, Protor(:,3), '-r', 'LineWidth', 3)

legend('turbine upstream','turbine middle','turbine downstream', ...
       'Location','best');
   
title('rotor power', 'FontSize', 16)
xlabel('time, t (s)', 'FontSize', 16);
ylabel('rotor power, P (W)', 'FontSize', 16);
   
set(gca,'FontSize', 16)
box on
grid on

%% Plot a histogram of Power
figure('Name', 'Rotor Power', ...
       'Color', 'white');
   


%% Plot the efficiency
figure('Name', 'Rotor Efficiency', ...
       'Color', 'white');
  
% plot(time, Protor ./ Pavail, 'LineWidth', 2)
hold on;
plot(time, Protor(:,1) ./ Pavail, '-b', 'LineWidth', 3)
plot(time, Protor(:,2) ./ Pavail, '-k', 'LineWidth', 3)
plot(time, Protor(:,3) ./ Pavail, '-r', 'LineWidth', 3)

legend('turbine upstream','turbine middle','turbine downstream', ...
       'Location','best');
   
title('rotor efficiency', 'FontSize', 16);
xlabel('time, t (s)', 'FontSize', 16);
ylabel('rotor efficiency, Cp', 'FontSize', 16);
   
axis([time(1) time(end) 0 1]);
set(gca,'FontSize', 16)
box on
grid on

%% Plot the relative power
figure('Name', 'Relative Rotor Power', ...
       'Color', 'white');
  
relative_power = Protor ./ repmat(Protor(:,1), 1, nTurbines);
% plot(time, relative_power, 'LineWidth', 2)
hold on;
plot(time, relative_power(:,1), '-b', 'LineWidth', 3)
plot(time, relative_power(:,2), '-k', 'LineWidth', 3)
plot(time, relative_power(:,3), '-r', 'LineWidth', 3)


legend('turbine upstream','turbine middle','turbine downstream', ...
       'Location','best');
   
title('Relative Rotor Power', 'FontSize', 16)
xlabel('time, t (s)', 'FontSize', 16);
ylabel('relative rotor power, P_{i} / P_{upstream}', 'FontSize', 16);
   
axis([time(1) time(end) 0 1])
set(gca,'FontSize', 16)
box on
grid on

%% the FFT with correct scaling
% http://math.stackexchange.com/questions/636847/understanding-fourier-transform-example-in-matlab

% signal = Protor(:,1);
% Fs     = 1000;                    % Sampling frequency
% 
% L      = time(end) - time(1);       % Sample time
% 
% N      = numel(signal);
% 
% 
% NFFT   = 2^nextpow2(L); % Next power of 2 from length of y
% 
% Y = fft(signal, NFFT)/Fs; % The Correct Scaling
% f    = Fs/2*linspace(0, 1, NFFT/2+1)';

%%
% figure('Name', 'spectra of rotor power', ...
%        'Color', 'white');
%    
% signal = Protor(:,1);
% fs     = 10;                    % Sampling frequency
% 
% N        = numel(signal);
% NFFT     = 2^nextpow2(L); % Next power of 2 from length of y
% X_mags   = abs( fft(signal, NFFT) );
% Y        = fft(signal, NFFT)/Fs; % The Correct Scaling
% bin_vals = (0 : N-1)';
% fax_Hz   = bin_vals*fs/N;
% N_2      = ceil(N/2);
% 
% plot(fax_Hz(1:N_2), X_mags(1:N_2))
% 
% title('Single-sided Magnitude spectrum (Hertz)');
% xlabel('Frequency (Hz)')
% ylabel('Magnitude');
% 
% set(gca,'xscale','log');
% set(gca,'yscale','log');
% box on
% grid on

%% 
% x  = Protor(:,1);
% Fs = 10;
% 
% N = length(x);
% xdft = fft(x);
% xdft = xdft(1:N/2+1);
% psdx = (1/(Fs*N)) * abs(xdft).^2;
% psdx(2:end-1) = 2*psdx(2:end-1);
% freq = 0:Fs/length(x):Fs/2;
% 
% plot(freq,10*log10(psdx))
% grid on
% title('Periodogram Using FFT')
% xlabel('Frequency (Hz)')
% ylabel('Power/Frequency (dB/Hz)')

% T = time(end) - time(1);



% NFFT = 2^nextpow2(N);        % Next power of 2 from length of input
% 
% p    = abs( fft(x) ) / (NFFT/2);
% pp   = p(1:NFFT/2).^2;
% freq = [0:NFFT/2-1] / T; 
% 
% semilogy(freq, pp);

% signal = Protor(:,1);
% N      = numel(signal);
% 
% X_mags   = abs( fft(signal) );
% bin_vals = (0:N-1)';
% fax_Hz = bin_vals*fs/N;
% N_2 = ceil(N/2);
% plot(fax_Hz(1:N_2), X_mags(1:N_2))
% xlabel('Frequency (Hz)')
% ylabel('Magnitude');
% title('Single-sided Magnitude spectrum (Hertz)');
% axis tight


%% calculate the FFT
Nsamples = numel(time);
% Fs   = 50;                   % sampling frequency
Fs = floor( 1 / (max(time)/Nsamples) );

N    = numel(time);
NFFT = 2^nextpow2(N);        % Next power of 2 from length of input
f    = Fs/2*linspace(0, 1, NFFT/2+1)';

% fft_power_1 = fft(Protor(:,1), NFFT) ./ Fs;
% fft_power_2 = fft(Protor(:,2), NFFT) ./ Fs;
% fft_power_3 = fft(Protor(:,3), NFFT) ./ Fs;
fft_power_1 = fft(Protor(:,1), NFFT) ./ N;   % absolute value of fft
fft_power_2 = fft(Protor(:,2), NFFT) ./ N;
fft_power_3 = fft(Protor(:,3), NFFT) ./ N;
% fft_power = fft(Protor, NFFT) ./ N;

% single-sided amplitude spectrum
% mag_fft_power_1 = 2*abs( fft_power_1(1:NFFT/2+1) );
% 
% % Plot single-sided amplitude spectrum.
% plot(f, mag_fft_power_1); 
% title('Single-Sided Amplitude Spectrum of y(t)')
% xlabel('Frequency (Hz)')
% ylabel('|Y(f)|')

% power spectral density
psd_power_1 = abs( fft_power_1(1:NFFT/2+1) ) ./ (f/2);
psd_power_2 = abs( fft_power_2(1:NFFT/2+1) ) ./ (f/2);
psd_power_3 = abs( fft_power_3(1:NFFT/2+1) ) ./ (f/2);
% psd_power = 2*abs( fft_power(1:NFFT/2+1,:) ) ./ f;

% plot the FFT
figure('Name', 'spectra of rotor power', ...
       'Color', 'white');
   
hold on;
% Plot single-sided amplitude spectrum.
% plot(f, 2*abs(fft_power_1(1:NFFT/2+1)), 'LineWidth', 2) 
% plot(f, 2*abs(fft_power_2(1:NFFT/2+1)), 'LineWidth', 2) 
% plot(f, 2*abs(fft_power_3(1:NFFT/2+1)), 'LineWidth', 2) 
plot(f, psd_power_1, '-b', 'LineWidth', 2) 
plot(f, psd_power_2, '-k','LineWidth', 2) 
plot(f, psd_power_3, '-r','LineWidth', 2)
% plot(f, psd_power, 'LineWidth', 2)

title('spectra of rotor power', 'FontSize', 16)
xlabel('frequency, f (Hz)', 'FontSize', 16);
ylabel('rotor power, PSD (W^2/Hz)', 'FontSize', 16);

legend('turbine upstream','turbine middle','turbine downstream', ...
       'Location','best');

set(gca,'xscale','log');
set(gca,'yscale','log');
set(gca,'FontSize', 16)
box on
grid on


%%
% INPUT VARIABLES:
%   x - Time series, [vector]
%   dt - Sampling Rate, [scalar]
%   win - Window, one of: 
%       'hanning', 'hamming', 'boxcar'
%   Nsg - Number of Segments (>=1)
%   pnv - Percentage Noverlap of Segments (0-100)
%   Nb - Band Averaging, number of bands to average
%   Wn - Cut-Off frequencies, used for filtering
%   ftype - Type of filter, 'high', 'low' or 'stop'
%   n - Number of coefficients to use in
%   the Butterworth filter

% x       = Protor(:,1);
% dt      = 10;                    % Sampling frequency
% w       = 'hanning';
% Nsg     = 2;
% pnv     = 50;
% Wn      = dt;
% ftype   = 'high';
% n       = 1;

% [psdf,conf,f] = specwelch(x,dt,w,Nsg,pnv,Wn,ftype,n)




%%
% x  = Protor(:,1);
% Fs     = 10;                    % Sampling frequency
% 
% N    = length(x);
% xdft = fft(x);
% xdft = xdft(1:N/2+1);
% psdx = (1/(Fs*N)) * abs(xdft).^2;
% psdx(2:end-1) = 2*psdx(2:end-1);
% freq = 0:Fs/length(x):Fs/2;
% 
% plot(freq,10*log10(psdx))
% grid on
% title('Periodogram Using FFT')
% xlabel('Frequency (Hz)')
% ylabel('Power/Frequency (dB/Hz)')

%% plot the filtered power
% 
% load bostemp
% days = (1:31*24)/24;
% plot(days, tempC), axis tight;
% ylabel('Temp (\circC)');
% xlabel('Time elapsed from Jan 1, 2011 (days)');
% title('Logan Airport Dry Bulb Temperature (source: NOAA)');
% 
% % In its simplest form, a moving average filter of length N takes the 
% % average of every N consecutive samples of the waveform.
% % To apply a moving average filter to each data point, we construct our 
% % coefficients of our filter so that each point is equally weighted and 
% % contributes 1/24 to the total average. This gives us the average 
% % temperature over each 24 hour period.
% hoursPerDay = 24;
% coeff24hMA = ones(1, hoursPerDay)/hoursPerDay;
% 
% avg24hTempC = filter(coeff24hMA, 1, tempC);
% plot(days, [tempC avg24hTempC]);
% legend('Hourly Temp','24 Hour Average (delayed)','location','best');
% ylabel('Temp (\circC)');
% xlabel('Time elapsed from Jan 1, 2011 (days)');
% title('Logan Airport Dry Bulb Temperature (source: NOAA)');
% 
% 
% %%
% figure
% 
% k = 3
% samplesPerSecond = ceil( Nsamples * 100);
% coeff_0p5hz_MA = ones(1, samplesPerSecond)/samplesPerSecond;
% 
% Power_filter = filter(coeff24hMA, 1, Protor(:,k));
% plot(time, [Protor(:,k) Power_filter]);
% % legend('upstream', ...
% %        'middle', ...
% %        'downstream', ...
% %        'location','best');
% ylabel('rotor power, P (W)');
% xlabel('time, t (s)');
% title('Filtered Rotor Power');
% 



%% estimate time that fastFlume needed to complete
% dw          = 0.02;     % write interval
% T           = 20;       % total simulation time in seconds
% timePerIter = mean([46 39 36 41 42 43 49 54 60 53].*60);    % minutes converted to seconds
% iters       = T / dw;    % number of write iterations
% 
% time_to_wait = fprintf(1, 'time_to_wait = %g hours \n', iters*timePerIter/3600);















%%
%parameters for figure and panel size
plotheight=20;
plotwidth=16;
subplotsx=3;
subplotsy=5;   
leftedge=1.2;
rightedge=0.4;   
topedge=1;
bottomedge=1.5;
spacex=0.2;
spacey=0.2;
fontsize=5;    
sub_pos=subplot_pos(plotwidth,plotheight,leftedge,rightedge,bottomedge,topedge,subplotsx,subplotsy,spacex,spacey);
 
%setting the Matlab figure
f=figure('visible','on')
clf(f);
set(gcf, 'PaperUnits', 'centimeters');
set(gcf, 'PaperSize', [plotwidth plotheight]);
set(gcf, 'PaperPositionMode', 'manual');
set(gcf, 'PaperPosition', [0 0 plotwidth plotheight]);
 
%loop to create axes
for i=1:subplotsx
for ii=1:subplotsy
 
ax=axes('position',sub_pos{i,ii},'XGrid','off','XMinorGrid','off','FontSize',fontsize,'Box','on','Layer','top');
 
z=peaks;
contour(z);
 
if ii==subplotsy
title(['Title (',num2str(i),')'])
end
 
if ii>1
set(ax,'xticklabel',[])
end
 
if i>1
set(ax,'yticklabel',[])
end
 
if i==1
ylabel(['Ylabel (',num2str(ii),')'])
end
 
if ii==1
xlabel(['Ylabel (',num2str(i),')'])
end
 
end
end
 
%Saving eps with matlab and then marking pdf and eps and png with system commands
filename=['test'];
print(gcf, '-depsc2','-loose',[filename,'.eps']);
system(['epstopdf ',filename,'.eps'])
system(['convert -density 300 ',filename,'.eps ',filename,'.png'])

function [ positions ] = subplot_pos(plotwidth,plotheight,leftmargin,rightmargin,bottommargin,topmargin,nbx,nby,spacex,spacey)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
 
    subxsize=(plotwidth-leftmargin-rightmargin-spacex*(nbx-1.0))/nbx;
    subysize=(plotheight-topmargin-bottommargin-spacey*(nby-1.0))/nby;
 
    for i=1:nbx
       for j=1:nby
 
           xfirst=leftmargin+(i-1.0)*(subxsize+spacex);
           yfirst=bottommargin+(j-1.0)*(subysize+spacey);
 
           positions{i,j}=[xfirst/plotwidth yfirst/plotheight subxsize/plotwidth subysize/plotheight];
 
       end
    end
end





