


% 512x512
a=imread('baboon.jpg');
b=jpeg_encode(a);
c=jpeg_decode(b);
subplot(1,3,3)
[x,y]=hist(reshape(b,1,length(b)^2),length(unique(b)));colormap('default')
x=x./sum(x);
plot(y,x)
subplot(1,3,1)
imagesc(a),colormap('gray'), axis square
title('original')
subplot(1,3,2)
imagesc(c),colormap('gray'), axis square
title('reconstructed')
pause

% 256x256
a=imread('house.jpg');
b=jpeg_encode(a);
c=jpeg_decode(b);
subplot(1,3,3)
[x,y]=hist(reshape(b,1,length(b)^2),length(unique(b)));colormap('default')
x=x./sum(x);
plot(y,x)
subplot(1,3,1)
imagesc(a),colormap('gray'), axis square
title('original')
subplot(1,3,2)
imagesc(c),colormap('gray'), axis square
title('reconstructed')
pause

% 128x128
a=imread('lena.jpg');
b=jpeg_encode(a);
c=jpeg_decode(b);
subplot(1,3,3)
[x,y]=hist(reshape(b,1,length(b)^2),length(unique(b)));colormap('default')
x=x./sum(x);
plot(y,x)
subplot(1,3,1)
imagesc(a),colormap('gray'), axis square
title('original')
subplot(1,3,2)
imagesc(c),colormap('gray'), axis square
title('reconstructed')
