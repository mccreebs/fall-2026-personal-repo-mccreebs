function plateLoaderMenuControl(s)
while(1)
    switch(menu('Choose command','Reset','X-Axis',...
            'Z-Axis','Gripper','Move','Status','Special Moves','Exit'))
        case 1
            writeline(s,'RESET');
        case 2
            writeline(s,['X-AXIS ',num2str(menu('Choose location to move to','1','2','3','4','5'))]);
        case 3
            switch(menu('Z-AXIS:','EXTEND','RETRACT'))
                case 1
                    writeline(s,'Z-AXIS EXTEND');
                case 2
                    writeline(s,'Z-AXIS RETRACT');
            end

        case 4
            switch(menu('GRIPPER:','OPEN','CLOSE'))
                case 1
                writeline(s,'GRIPPER OPEN');
                case 2
                    writeline(s,'GRIPPER CLOSE');
            end

        case 5
            prompt = {'Enter starting location','Enter final location'};
            dlgtitle = 'Input';
            fieldsize = [1 45; 1 45];
            definput = {'1','2'};
            move = inputdlg(prompt,dlgtitle,fieldsize,definput);
            
            writeline(s,['MOVE ',num2str(move{1}), ' ', num2str(move{2})]);
            

        case 6
            writeline(s,'LOADER_STATUS');

        case 7
            switch(menu('Special Moves:','Choke Slam','Thank You'))
                case 1
                    uiwait(helpdlg('Please place plates at locations 1 and 3'));
                    writeline(s,'X-AXIS 1');
                    readline(s);
                    writeline(s,'GRIPPER OPEN');
                    readline(s);
                    writeline(s,'Z-AXIS EXTEND');
                    readline(s);
                    writeline(s,'GRIPPER CLOSE');
                    readline(s);

                    writeline(s,'Z-AXIS RETRACT');
                    readline(s);
                    writeline(s,'X-AXIS 5');
                    readline(s);
                    writeline(s,'Z-AXIS EXTEND');
                    readline(s);
                    writeline(s,'GRIPPER OPEN');
                    readline(s);
                    writeline(s,'Z-AXIS RETRACT');
                    readline(s);

                    writeline(s,'X-AXIS 3');
                    readline(s);
                    writeline(s,'Z-AXIS EXTEND');
                    readline(s);
                    writeline(s,'GRIPPER CLOSE');
                    readline(s);

                    writeline(s,'Z-AXIS RETRACT');
                    readline(s);
                    writeline(s,'X-AXIS 5');
                    readline(s);
                    writeline(s,'GRIPPER OPEN');
                    readline(s);

                case 2
                    writeline(s,'Z-AXIS RETRACT');
            end

        case 8
            fprintf("Goodbye!\n");
            break
    end
    
    readline(s)
end
end

