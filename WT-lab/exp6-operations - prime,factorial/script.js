function fact()
        {
            var num1=parseInt(document.getElementById("a").value);
            var sum=1,i;
            for(i=1;i<=num1;i++)
            {
                sum=sum*i;
            }
            document.getElementById("answer").value=sum;
           
        }
        function fib()
        {
            var num1=parseInt(document.getElementById("a").value);
            var u=1,v=1,sum=0;
            const my = new Array();
            my.push(1);
            my.push(1);
            while(u<=num1 && u+sum<=num1)
            {
                sum=u+v;
                u=v;
                v=sum;
                my.push(sum);
            }
            document.getElementById("answer").value=my;
        }
        function pali()
        {
            var num1=parseInt(document.getElementById("a").value);
            var sum=0,temp=num1;
            while(num1!=0)
            {
                sum=(sum*10)+(num1%10);
                num1=Math.floor(num1/10);
            }
            if(temp == sum)
            document.getElementById("answer").value="Palindrome";
            else
            document.getElementById("answer").value= "Not Palindrome";
            
        }
        function prime()
        {
            var num1=parseInt(document.getElementById("a").value);
            if(num1<1)
            document.getElementById("answer").value= "Not prime number";
            else if(num1==1)
            document.getElementById("answer").value= "Neither Prime Nor Composite";
            else
            {
                var i,c=0;
                for(i=1;i<=Math.floor(num1/2);i++)
                {
                    if(num1%i==0)
                    c++;
                }
                if(c>1)
                document.getElementById("answer").value= "Not prime number";
                else
                document.getElementById("answer").value= "prime number";
            }
           
        }
        function reset()
        {
            document.getElementById("a").value=null;
            document.getElementById("answer").value=null;
        }