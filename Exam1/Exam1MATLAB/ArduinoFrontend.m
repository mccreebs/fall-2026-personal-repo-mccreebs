classdef ArduinoFrontend < hgsetget
    %PLATELOADER Controls the Beckman Coulter Plate Loader Robot
    %   Performs the basic actions to control the plate loader

    methods

        function response = sendLEDCommand(obj, command)
            import matlab.net.*
            import matlab.net.http.*

            r = RequestMessage;
            uri = URI("http://sinclaer-pi5.rose-hulman.edu:8081/api/led" + command);
            resp = send(r,uri);
            response = resp.Body.Data;

            fprintf("Response to %s --> %s", command, response);
        end

        function response = sendFLASHCommand(obj, num, period)
            import matlab.net.*
            import matlab.net.http.*

            r = RequestMessage;
            uri = URI("http://sinclaer-pi5.rose-hulman.edu:8081/api/flash" + num, "/" + period);
            resp = send(r,uri);
            response = resp.Body.Data;

            fprintf("Response to %s --> %s", command, response);
        end

    end

end