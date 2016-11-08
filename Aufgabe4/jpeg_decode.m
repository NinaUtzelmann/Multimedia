function out=jpeg_decode(in)

% function out=jpeg_decode(in)
%
% function to demonstrate the jpeg decoding
%
%   in  :   matrix with quantised DCT values
%   out :   reconstructed image


% DCT matrix
T=0.5*cos([0:7]'*(2*[0:7]+1)*pi/16);
