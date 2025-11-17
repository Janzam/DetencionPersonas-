""""""

Ejecutor de todas las pruebasScript para ejecutar todas las pruebas del proyecto

Ejecuta pruebas unitarias, de integración y funcionalesUso: python tests/run_all_tests.py

""""""

import unittest

import unittestimport sys

import sysimport os

import os

# Agregar el directorio raíz al path

# Agregar el directorio raíz al pathsys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Importar los módulos de prueba

# Importar suites de pruebasfrom tests import test_unitarios

from tests import test_unitariosfrom tests import test_integracion

from tests import test_integracionfrom tests import test_funcionales

from tests import test_funcionales



def run_all_tests():

def main():    """Ejecutar todas las suites de pruebas"""

    """Ejecutar todas las suites de pruebas"""    

    print("=" * 70)    # Crear el runner

    print("EJECUTANDO TODAS LAS PRUEBAS DEL SISTEMA")    runner = unittest.TextTestRunner(verbosity=2)

    print("=" * 70)    

        # Suite principal

    # Crear suite principal    main_suite = unittest.TestSuite()

    suite_principal = unittest.TestSuite()    

        print("\n")

    # Agregar suites individuales    print("=" * 80)

    print("\n1. Agregando pruebas unitarias...")    print(" SUITE COMPLETA DE PRUEBAS - DETECCIÓN DE PERSONAS CON YOLOV8")

    suite_principal.addTest(test_unitarios.suite())    print("=" * 80)

        print("\n")

    print("2. Agregando pruebas de integración...")    

    suite_principal.addTest(test_integracion.suite())    # 1. Pruebas Unitarias

        print("-" * 80)

    print("3. Agregando pruebas funcionales...")    print(" 1. PRUEBAS UNITARIAS (sin dependencias externas)")

    suite_principal.addTest(test_funcionales.suite())    print("-" * 80)

        suite_unitarias = test_unitarios.suite()

    # Ejecutar todas las pruebas    resultado_unitarias = runner.run(suite_unitarias)

    print("\n" + "=" * 70)    

    print("INICIANDO EJECUCIÓN DE PRUEBAS")    # 2. Pruebas de Integración

    print("=" * 70 + "\n")    print("\n")

        print("-" * 80)

    runner = unittest.TextTestRunner(verbosity=2)    print(" 2. PRUEBAS DE INTEGRACIÓN (con YOLO real y OpenCV)")

    result = runner.run(suite_principal)    print("-" * 80)

        suite_integracion = test_integracion.suite()

    # Resumen final    resultado_integracion = runner.run(suite_integracion)

    print("\n" + "=" * 70)    

    print("RESUMEN DE PRUEBAS")    # 3. Pruebas Funcionales

    print("=" * 70)    print("\n")

    print(f"Pruebas ejecutadas: {result.testsRun}")    print("-" * 80)

    print(f"Éxitos: {result.testsRun - len(result.failures) - len(result.errors) - len(result.skipped)}")    print(" 3. PRUEBAS FUNCIONALES (end-to-end del sistema completo)")

    print(f"Fallos: {len(result.failures)}")    print("-" * 80)

    print(f"Errores: {len(result.errors)}")    suite_funcionales = test_funcionales.suite()

    print(f"Omitidas: {len(result.skipped)}")    resultado_funcionales = runner.run(suite_funcionales)

    print("=" * 70)    

        # Resumen final

    # Retornar código de salida apropiado    print("\n")

    return 0 if result.wasSuccessful() else 1    print("=" * 80)

    print(" RESUMEN DE RESULTADOS")

    print("=" * 80)

if __name__ == '__main__':    

    sys.exit(main())    total_tests = (resultado_unitarias.testsRun + 

                   resultado_integracion.testsRun + 
                   resultado_funcionales.testsRun)
    
    total_failures = (len(resultado_unitarias.failures) + 
                      len(resultado_integracion.failures) + 
                      len(resultado_funcionales.failures))
    
    total_errors = (len(resultado_unitarias.errors) + 
                    len(resultado_integracion.errors) + 
                    len(resultado_funcionales.errors))
    
    total_skipped = (len(resultado_unitarias.skipped) + 
                     len(resultado_integracion.skipped) + 
                     len(resultado_funcionales.skipped))
    
    print(f"\nPruebas Unitarias:")
    print(f"  - Ejecutadas: {resultado_unitarias.testsRun}")
    print(f"  - Fallidas: {len(resultado_unitarias.failures)}")
    print(f"  - Errores: {len(resultado_unitarias.errors)}")
    print(f"  - Omitidas: {len(resultado_unitarias.skipped)}")
    
    print(f"\nPruebas de Integración:")
    print(f"  - Ejecutadas: {resultado_integracion.testsRun}")
    print(f"  - Fallidas: {len(resultado_integracion.failures)}")
    print(f"  - Errores: {len(resultado_integracion.errors)}")
    print(f"  - Omitidas: {len(resultado_integracion.skipped)}")
    
    print(f"\nPruebas Funcionales:")
    print(f"  - Ejecutadas: {resultado_funcionales.testsRun}")
    print(f"  - Fallidas: {len(resultado_funcionales.failures)}")
    print(f"  - Errores: {len(resultado_funcionales.errors)}")
    print(f"  - Omitidas: {len(resultado_funcionales.skipped)}")
    
    print(f"\n{'='*80}")
    print(f" TOTAL DE PRUEBAS: {total_tests}")
    print(f" Exitosas: {total_tests - total_failures - total_errors}")
    print(f" Fallidas: {total_failures}")
    print(f" Errores: {total_errors}")
    print(f" Omitidas: {total_skipped}")
    print(f"{'='*80}\n")
    
    # Retornar código de salida apropiado
    if total_failures > 0 or total_errors > 0:
        return 1
    return 0


if __name__ == '__main__':
    exit_code = run_all_tests()
    sys.exit(exit_code)
