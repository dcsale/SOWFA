%% start clean
close all
clear all

% add external dependencies
addpath([pwd filesep 'sort_nat']);

%% ===================================================================== %%
%  _   _ ____  _____ ____      ___ _   _ ____  _   _ _____ ____           %
% | | | / ___|| ____|  _ \    |_ _| \ | |  _ \| | | |_   _/ ___|          %
% | | | \___ \|  _| | |_) |    | ||  \| | |_) | | | | | | \___ \          % 
% | |_| |___) | |___|  _ <     | || |\  |  __/| |_| | | |  ___) |         %
%  \___/|____/|_____|_| \_\   |___|_| \_|_|    \___/  |_| |____/          %
% ======================================================================= %
%% specify directory and filenames to load

% this file has info on mesh dimensions, spatial and temporal resolution
file_info = '/mnt/data-RAID-1/danny/fastFlume-RC5_Turbine=LabScale1_Layout=SingleRotor_TSR=6.2_Mesh=medium/VisIt-output/slices/mesh-info.txt';

% directory containing list of files for 2D slices exported from VisIt into Xmdv format
% dir_data  = '/mnt/data-RAID-1/danny/fastFlume-RC5_Turbine=LabScale1_Layout=SingleRotor_TSR=6.2_Mesh=medium/VisIt-output/slices/plane-yz_x=+1D/Ux';
% dir_data  = '/mnt/data-RAID-1/danny/fastFlume-RC5_Turbine=LabScale1_Layout=SingleRotor_TSR=6.2_Mesh=medium/VisIt-output/slices/plane-yz_x=+1D/Uy';
% dir_data  = '/mnt/data-RAID-1/danny/fastFlume-RC5_Turbine=LabScale1_Layout=SingleRotor_TSR=6.2_Mesh=medium/VisIt-output/slices/plane-yz_x=+1D/Uz';
% dir_data  = '/mnt/data-RAID-1/danny/fastFlume-RC5_Turbine=LabScale1_Layout=SingleRotor_TSR=6.2_Mesh=medium/VisIt-output/slices/plane-yz_x=+1D/Umag';
dir_data  = '/mnt/data-RAID-1/danny/fastFlume-RC5_Turbine=LabScale1_Layout=SingleRotor_TSR=6.2_Mesh=medium/VisIt-output/slices/plane-yz_x=-2D/Ux';


% ======================================================================= %
% End User Inputs                                                         %
% ======================================================================= %

%% read data from the mesh info file
file_ID   = fopen(file_info, 'r');
format    = '%f %f %f %f %f %f %f';
data_mesh = textscan(file_ID, format, 'HeaderLines', 1);
fclose(file_ID);

% reshape the data
Lx   = data_mesh{1};    % length of domain in x (meters)
Ly   = data_mesh{2};
Lz   = data_mesh{3};
Nx   = data_mesh{4};    % number cells in x
Ny   = data_mesh{5};
Nz   = data_mesh{6};
dt_w = data_mesh{7};    % time interval of slices (seconds)

%% get the list of filenames, and sort them sequentially, cannot rely on 'dir' to 
%  return the file list in sequential order
files        = dir( [dir_data filesep '*.okc'] );   % list all files in the *.okc Xdmv format
files        = {files.name};                        % shape into a nicer list
[fsort, ind] = sort_nat(files, 'ascend');           % sort the file list with natural ordering
files_sorted = fsort(:);

%% loop through each file and store within array containing all time steps

% allocate an array to contain all time steps
X = zeros( Ny+1, Nz+1, numel(files_sorted) );
Y = zeros( Ny+1, Nz+1, numel(files_sorted) );
Z = zeros( Ny+1, Nz+1, numel(files_sorted) );
U = zeros( Ny+1, Nz+1, numel(files_sorted) );
t = zeros(numel(files_sorted), 1); 

for n = 1:numel(files_sorted)
    
    % read data from Xmdv file
    file_ID     = fopen([dir_data filesep files_sorted{n}], 'r');
    format      = '%f %f %f %f';
    data_scalar = textscan(file_ID, format, 'HeaderLines', 9);
    fclose(file_ID);
    
    % reshape the data
    x  = data_scalar{1};
    y  = data_scalar{2};
    z  = data_scalar{3};
    u  = data_scalar{4};

    % streamwise slices were made in the Y-Z plane, reshape accordingly
    xx = reshape(x, [Ny+1, Nz+1]);
    yy = reshape(y, [Ny+1, Nz+1]);
    zz = reshape(z, [Ny+1, Nz+1]);
    uu = reshape(u, [Ny+1, Nz+1]);

    % make some corrections to data
    % this is because of some bug when slicing the VTK files ... for some
    % reason the mesh ordering of the first 2 rows/columns are always in wrong order
    % and contain duplicate values ... for now just eliminate these boundary
    % values ... not sure whose fault this is, either OpenFOAM, VisIt, or VTK.
    % So, mask the 1st two columns:
    xx(:, 1:2) = NaN;
    yy(:, 1:2) = NaN;
    zz(:, 1:2) = NaN;
    uu(:, 1:2) = NaN;

    % add current time step into 3-dim array
    X(:, :, n) = xx;
    Y(:, :, n) = yy;
    Z(:, :, n) = zz;
    U(:, :, n) = uu;
    t(n)       = n*dt_w; % the zero time step is not saved
    
end

%% plot the data

% n = 1:numel(files_sorted); 	% this will plot every time step, dont do this unless you want too many figures!
% n = [1 2 3 10 20];         	% just plot these time steps
n = 1:33:numel(t);        	% just plot these time steps

for m = 1:numel(n)
    
    figure('color', 'white');

    % ======================================================================= %
    subplot(2, 1, 1)

    pcolor(Y(:,:,n(m)), Z(:,:,n(m)), U(:,:,n(m)))

    % add labels
    title( [files_sorted{n(m)} ', time = ' num2str(t(n(m))) ' (s)'] , ...
          'interpreter','none', ...
           'FontSize',10)
    xlabel('crossflow, y (m)', ...
           'FontSize',10)
    ylabel('depth, z (m)', ...
           'FontSize',10)
    cb = colorbar;
    ylabel(cb, 'streamwise velocity, Ux (m/s)', ...
           'FontSize',10)

    % adjust appearance
    set(gca,'FontSize',10)
    box on
    axis equal
    axis([min(y) max(y) min(z) max(z)])
    shading interp

    % ======================================================================= %
    subplot(2, 1, 2)

    surf(Y(:,:,n(m)), Z(:,:,n(m)), U(:,:,n(m)))

    % add labels
    title( [files_sorted{n(m)} ', time = ' num2str(t(n(m))) ' (s)'] , ...
          'interpreter','none', ...
           'FontSize',10)    
    xlabel('crossflow, y (m)', ...
           'FontSize',10)
    ylabel('depth, z (m)', ...
           'FontSize',10)
    zlabel('streamwise velocity, Ux (m/s)', ...
           'FontSize',10)
    cb = colorbar;
    ylabel(cb, 'streamwise velocity, Ux (m/s)', ...
           'FontSize',10);

    % adjust appearance
    set(gca,'FontSize',10)
    box on
    shading interp
    camlight headlight;
    lighting gouraud
    axis vis3d
    set(gcf, 'renderer', 'zbuffer')

    % set only the x and y axes to be equal (z still gets scaled)
    set(gca, 'DataAspectRatio', [diff(get(gca, 'XLim')) diff(get(gca, 'XLim')) diff(get(gca, 'ZLim'))])

end % for

