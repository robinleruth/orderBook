import { Component, OnInit } from '@angular/core';
import { OrderBookService } from '../order-book.service';

@Component({
  selector: 'app-order-book',
  templateUrl: './order-book.component.html',
  styleUrls: ['./order-book.component.scss']
})
export class OrderBookComponent implements OnInit {

  constructor(private orderBookService: OrderBookService) { }

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
          console.log(n);
      });
  }

}
