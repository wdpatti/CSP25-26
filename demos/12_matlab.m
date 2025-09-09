clc;
clear;

decimalNumber = input('Enter a whole number: ');
if mod(decimalNumber, 1) ~= 0
    %error('Please enter a valid whole number.');
end


binaryNumber = dec2bin(decimalNumber);



fprintf('The binary representation of %d is: %s\n', decimalNumber, binaryNumber);
fprintf('Binary form: %s\n', binaryNumber);