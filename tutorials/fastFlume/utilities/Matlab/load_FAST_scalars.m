function [time, varName] = load_FAST_scalars(dir_TurbineOutput, ...
                                             data_filename, ...
                                             numCols, ...
                                             nHeaders, ...
                                             restart_folders, ...
                                             idTurbine, ...
                                             perStart, ...
                                             perEnd)
% this file reads all the restart directories from the FAST output, and 
% then joins all data into a single time series.  And then can optionally
% return only a subset of that time series.



% begin function: AND dont use hardcoded variable names!
turbine_id  = [];
t           = [];
dt          = [];
tmp_varName = [];
% data = cell(1, numel(restart_folders));
for n = 1:numel(restart_folders)
    
    datafile = [dir_TurbineOutput filesep restart_folders{n} filesep data_filename]
    
    fid = fopen(datafile, 'r');
    if fid == -1
        error(['ERROR: Could not locate and open file ' datafile]);
    end

    % skip the header lines
    for j = 1:nHeaders
        fgetl(fid);
    end
    
    % read the data
    tmp  = {textscan(fid, repmat('%f ', 1, numCols), 'CollectOutput', 0)};
    data = cell2mat(tmp{:});
    
    % removing duplicate time steps, use the most recent duplicates
    if n > 1    % there can be duplicate time values      
        t_restart = data(1,2);  
        ii        = find(t >= t_restart, 1);
        
        % trim any duplicate values from previous time folder
        turbine_id  =  turbine_id(1:ii);
        t           =           t(1:ii);
        dt          =          dt(1:ii);
        tmp_varName = tmp_varName(1:ii);
        
    end
    
    % append the next restart folder data to previous (no duplicates)
    turbine_id  = [ turbine_id; data(:,1)];
    t           = [          t; data(:,2)];
    dt          = [         dt; data(:,3)];
    tmp_varName = [tmp_varName; data(:,4)];

    % close the file
    fclose(fid);
end


%% separate the data series by turbine identification
for n = 1:numel(idTurbine)
    index        = turbine_id == idTurbine(n);
    varName(:,n) = tmp_varName(index);
end

% all turbines share common time
time = t(:,1);
time = time(turbine_id == idTurbine(1));

%% only take subset of data
Nsamples = numel(time);
Nstart   = max(floor(Nsamples*perStart), 1);        % otherwise start at first sample point
Nend     = max(ceil(Nsamples*perEnd), Nsamples);    % otherwise use to final sample point

%% return output
time    =  time(Nstart:Nend, 1);
varName = varName(Nstart:Nend, :);

end % function

