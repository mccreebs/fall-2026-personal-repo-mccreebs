classdef MyShape < handle
    
    properties
        Patch
    end

    methods
        function obj = MyShape(xCoords, yCoords, color)
            obj.Patch = patch(xCoords, yCoords, color);

        end

        function move(obj, dx, dy)
            % TODO: Implement a move method
            obj.Patch.XData = obj.Patch.XData + dx;
            obj.Patch.YData = obj.Patch.YData + dy;
        end
    end
end