# Bot de Votação no Discord 🎮📊

Um bot no Discord programado em **Python** que realiza votações entre dois candidatos dentro de um chat específico. As informações dos votos são registradas e enviadas para o **vMix**, onde são exibidas em tempo real para a audiência.

## 📌 Como funciona?
1. Os usuários votam digitando a sigla dos candidatos no chat. 
   - Exemplo: `GF` para *Gravity Falls* e `APS` para *Apenas um Show*.

  <img src="/assets/download.gif" alt="Discord Exemplo">

2. O bot contabiliza os votos e gera um arquivo `.json` com os resultados:
   ```json
   {
       "Opção": "Apenas um Show",
       "Votos": 5,
       "Porcentagem": "71.4%"
   },
   {
       "Opção": "Gravity Falls",
       "Votos": 2,
       "Porcentagem": "28.6%"
   }
   ```
3. Esses dados são enviados para o **vMix**, onde são atualizados automaticamente para exibição em tempo real.

## 🎭 Inspirado no Votatoon!
Esse projeto é inspirado no antigo programa do **Cartoon Network**, o *Votatoon*, onde o público escolhia entre dois desenhos e o vencedor era exibido na programação. 

![Votatoon](https://static.wikia.nocookie.net/cartoon-nexus/images/2/2b/Votatoon.png/)

## 🎥 Integração com vMix
Os resultados das votações são enviados automaticamente para o **vMix**, um software profissional de transmissão ao vivo, garantindo que a audiência veja as atualizações em tempo real. 

![vMix](https://upload.wikimedia.org/wikipedia/en/2/2b/VMix_logo.png)

## 🚀 Como usar?
1. **Configure o bot** no seu servidor do Discord.
2. **Defina o chat específico** para a votação.
3. **Inicie a votação** e acompanhe os resultados ao vivo no vMix!

🔧 *Este projeto ainda está em desenvolvimento. Contribuições são bem-vindas!*
