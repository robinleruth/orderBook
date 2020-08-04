import { Component, OnInit } from '@angular/core';
import { OrderBookService } from '../order-book.service';
import { Price } from '../model/price';

@Component({
  selector: 'app-order-book',
  templateUrl: './order-book.component.html',
  styleUrls: ['./order-book.component.scss']
})
export class OrderBookComponent implements OnInit {
    prices: Price[] = [];

  constructor(private orderBookService: OrderBookService) { }

  columnDefs = [
        {headerName: 'Ticker', field: 'ticker' },
        {headerName: 'Bid', field: 'bid' },
        {headerName: 'Ask', field: 'ask'}
    ];

    rowData;

  ngOnInit(): void {
      (function(that){
          setInterval(function(){
              that.getBestPrices();
          }, 
          1000);
      })(this);
  }

  getBestPrices(): void {
      this.orderBookService.getBestPrices().subscribe(n => {
          this.prices = n;
          this.rowData = n;
          console.log(this.prices);
      });
  }

}
