#include <iostream>
using namespace std;

int main () {

    // Programa para analizar la temperatura maxima semanal.


    int week_temps[7] = {0};
    int high_temps = 0;
    int prom_temps = 0;

    cout << "------------------------------------------------------" << endl;
    cout << "Ingrese las temperaturas (Cº) máximas de cada dia: " << endl;
    cout << endl;
    for (int i = 0; i < 7; i++){
        cout << "Dia " << i + 1 <<" : ";
        cin >> week_temps[i];
    }
    cout << "------------------------------------------------------" << endl;

    for(int i = 0; i < 7; i++){
        if(week_temps[i] > 35){
            high_temps++;
        }
    }

    for(int i = 0; i < 7; i++){
        prom_temps += week_temps[i];
    }
    prom_temps = prom_temps / 7;

    cout << "En la semana " << high_temps << " días fueron mayores a 35Cº" << endl;
    cout << "Promedio de temperatura en la semana: " << prom_temps << "Cº" << endl;

    if(prom_temps > 30){
        cout << "Semana calurosa." << endl;
    }else if (prom_temps <= 30){
        cout << "Semana templada." << endl;
    }


    return 0;
}