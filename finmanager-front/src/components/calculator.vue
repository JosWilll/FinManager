<template>
    <div>
        <table class="calculator">
            <tbody>
                <tr>
                <td colspan="3"><input type="text" id="prompt"></td>
                <td><input type="button" class="btn-primary" value="C" @click="erase()"></td>
                </tr>
                <tr>
                <td><input type="button" class="btn-primary" value="1" @click="calcInput('1')"></td>
                <td><input type="button" class="btn-primary" value="2" @click="calcInput('2')"></td>
                <td><input type="button" class="btn-primary" value="3" @click="calcInput('3')"></td>
                <td><input type="button" class="btn-primary" value="/" @click="calcInput('/')"></td>
                </tr>
                <tr>
                <td><input type="button" class="btn-primary" value="4" @click="calcInput('4')"></td>
                <td><input type="button" class="btn-primary" value="5" @click="calcInput('5')"></td>
                <td><input type="button" class="btn-primary" value="6" @click="calcInput('6')"></td>
                <td><input type="button" class="btn-primary" value="*" @click="calcInput('*')"></td>
                </tr>
                <tr>
                <td><input type="button" class="btn-primary" value="7" @click="calcInput('7')"></td>
                <td><input type="button" class="btn-primary" value="8" @click="calcInput('8')"></td>
                <td><input type="button" class="btn-primary" value="9" @click="calcInput('9')"></td>
                <td><input type="button" class="btn-primary" value="-" @click="calcInput('-')"></td>
                </tr>
                <tr>
                <td><input type="button" class="btn-primary" value="0" @click="calcInput('0')"></td>
                <td><input type="button" class="btn-primary" value="." @click="calcInput('.')"></td>
                <td><input type="button" class="btn-primary" value="=" @click="calculate()"></td>
                <td><input type="button" class="btn-primary" value="+" @click="calcInput('+')"></td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
    export default{
        name: 'calculator-item',
        methods: {
            // Adds char to calculator input prompt
            calcInput(char){
            let prompt = document.getElementById("prompt");
            prompt.value += char;
            },

            // Calculates the result for calc prompt input
            calculate(){
                let prompt = document.getElementById("prompt");

                // RegEx to check if calculator prompt has anything 
                // besides digits or mathematical operators
                let calcChecker = /[^\d+\-*/]/g;
                if(calcChecker.test(prompt.value)){
                    alert("Calculator input has wrong characters!");
                    return;
                }

                // Tokenize prompt to divide into an  
                // array of operators and operands
                let tokens = prompt.value.split(/([+\-*/])/);

                // First to check multiplying and division
                for(let i=0;i<tokens.length;i++){
                    switch(tokens[i]){
                    case '*':
                        tokens[i-1] = Number(tokens[i-1]) * Number(tokens[i+1]);
                        tokens.splice(i, 2);
                        i-=2;
                        break;
                    case '/':
                        tokens[i-1] = Number(tokens[i-1]) / Number(tokens[i+1]);
                        tokens.splice(i, 2);
                        i-=2;
                        break;
                    }
                }
                for(let i=0; i<tokens.length;i++){
                    switch(tokens[i]){
                    case '+':
                        tokens[i-1] = Number(tokens[i-1]) + Number(tokens[i+1]);
                        tokens.splice(i, 2);
                        i-=2;
                        break;
                    case '-':
                        tokens[i-1] = Number(tokens[i-1]) - Number(tokens[i+1]);
                        tokens.splice(i,2);
                        i-=2;
                        break;
                    }
                }
                prompt.value = tokens[0];
            },
            erase(){
                document.getElementById("prompt").value = "";
            }
        },
    }
</script>

<style>
  .calculator input[type="button"]{
    border-radius: 5px;
    width: 100%;
  }
</style>