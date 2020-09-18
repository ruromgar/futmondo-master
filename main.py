import pandas as pd

def transform_data(transfer):
    transfer = transfer.split('class="text"><strong>')[1]
    transfer = transfer.split('</strong></div></li><a class="icon-revert"></a></ul>')[0]
    transfer = transfer.replace(
        '</strong><time>', ' - ').replace(
        '</time><span>', ' - ').replace(
        '</span><div class="from">De <strong>', ' - ').replace(
        '</strong> a <strong>', ' - ')

    # At this point every transfer should look like: 
    # Antoñín - 17/09/2020 - 10:10 - 800.000 € - Equipo ESPAÑA - futmondo
    
    transfer_data = transfer.split(' - ')
    transfer_dict = {
        'player': transfer_data[0],
        'date': transfer_data[1],
        'time': transfer_data[2],
        'amount': transfer_data[3].replace('.', '').replace(' €', ''),
        'from': transfer_data[4],
        'to': transfer_data[5],
    }
    return transfer_dict
    
def main():
    with open('futmondo.html', 'r', encoding="utf8") as f:
        transfers = f.readlines()
        transfers = [x.strip() for x in transfers]

    transfers = [transform_data(t) for t in transfers]

    pd.DataFrame(transfers.items(), columns=['Player', 'Date', 'Time', 'Amount', 'From', 'To'])
    pd.to_csv('test.csv')

    #with open('futmondo_clean.html', 'a', encoding="utf8") as f:
    #    for t in transfers:
    #        f.write(f'{t}\n')

main()