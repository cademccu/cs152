import analyze
import report

def main():
    analyze.processFile(input('filename?\n'))
    report.reportData(analyze.getPlanets())

if __name__ == "__main__":
    main()
