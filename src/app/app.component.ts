import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'psiqly';

  email: string = '';
  onSubmit() {
    console.log('Correo electrónico enviado:', this.email);
    // Aquí iría la lógica para iniciar la evaluación psicológica
  }
}
