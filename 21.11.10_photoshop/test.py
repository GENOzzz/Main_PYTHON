draw = new ImagickDraw();

# 렌더링
image->drawImage($draw);



# path 그리기 시작
draw->pathStart();

# path 그리기 종료
draw->pathFinish();



# 색 설정
# 점선
draw->setStrokeColor($pixel);

# 색칠하기
draw->setFillColor($pixel);



#3텍스트
draw->setFontSize(20);
draw->setFont('aquafont.ttf');
draw->annotation($x, $y, 'Hello World');



# 포인트 이동
draw->pathMoveToAbsolute($x, $y); // 절대좌표
draw->pathMoveToRelative($x, $y);   // 상대좌표



# 직선
draw->pathLineToAbsolute($x, $y);
draw->pathLineToRelative($x, $y);




# 2차 베지에 곡선
draw->pathCurveToQuadraticBezierAbsolute($x1, $y1, $x, $y);
draw->pathCurveToQuadraticBezierRelative($x1, $y1, $x, $y);



##제어점을 지정하지 않고 미끄러지는 3차 베지에 곡선
draw->pathCurveToSmoothAbsolute($x2, $y2, $x, $y);
draw->pathCurveToSmoothRelative($x2, $y2, $x, $y);


