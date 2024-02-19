using Images
import Base: ~

~(x::RGB{N0f8}) = RGB{N0f8}(~x.r, ~x.g, ~x.b)

function g(i; r=1)
	H = Int(length(i[1,:])//2)
	A = i[:, 1:H]
	B = i[:, H+1:2H]
	if r == 1 (.~reverse(A), reverse(B)) else (A,B) end
end

function f(x, y; r=1)
	if length(x[1,:]) == 1 hcat(x, y)
	else
		(a, b) = g(x; r)
		(p, q) = g(y; r)
		hcat(
		     f(q, a; r),
		     f(b, p; r)
		     )
	end
end

h(i; r=1) = begin (x, y) = g(.~i); f(x, y; r) end

h(i,n; r=1) = if n == 0 i else h(h(i; r),n-1; r) end #unoptimized but do the job :P

function create_challenge()
	flag = load("./macos.png")		# takes the fucking  flag.png 
	print(flag)
	chall = h(flag, rand(20:30)) #Apply the transformation for 20~30 times :D
	# takes it fucking randomely
	save("./khtek.png", chall)
end

create_challenge()
