function convert_two_spots(number){
    return (Math.round(number * 100)/100).toFixed(2);
}
// Amortized loan
// Payment = Amount / Discount Facor
// D = {[(1 + r)n] - 1}/[r(1 + r)n]
// n = # of payments per year * loan term length
// r = APR/n
// example: loan of 10k at 3% for 7 years
// n = 84 (12 monthly payments/year * 7 years)
// r = 0.0025 (0.03/by 12 payments per year)
// D = 75.6813 {[(1+0.0025)84] - 1} / [0.0025(1+0.0025)84]
// P = $132.13 (10,000/75.6813)
// calculating the interest only payment on the above example:
// Payment = Amount * (APR/12)
// P = $25 (10,000 * (0.03/12))
function listen_for_input(e) {
    switch(e.target.name){
        case 'term':
            console.log("it's a term");
            break;
        case 'principle':
            console.log("it's a principle");
            break;
        case 'apr':
            console.log("it's a apr");
            break;
        default:
            console.log('None')
            break;
    }
    return
}
document.querySelector("input[name=principle]").addEventListener('input', listen_for_input);
document.querySelector("input[name=apr]").addEventListener('input', listen_for_input);
document.querySelector("input[name=term]").addEventListener('input', listen_for_input);
var principle = 0;
var apr = 0;
var term = 0;
