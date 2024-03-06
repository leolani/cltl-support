# cltl-support

This repo contains utilities related tot the Leolani application.

## Setup

Create a virtual environment and install the project dependencies:

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Log file inspection

### Timeline

`cltl.log_timline` contains a tool to visualize the processing times of
different events or timings between events. To create the visualization, in the
active virtual environment run

    python -m cltl.log_timeline.timeline --log <path/to.logfile>

The visualization will be opened in your default browser. A restricted set of
lanes from the result can be shown by adding the `--service`, e.g. like

    python -m cltl.log_timeline.timeline --log <path/to.logfile> --service AsrService Whisper

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any
contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- LICENSE -->

## License

Distributed under the MIT License. See [`LICENSE`](https://github.com/leolani/cltl-combot/blob/main/LICENCE) for more
information.


<!-- CONTACT -->

## Authors

* [Thomas Baier](https://www.linkedin.com/in/thomas-baier-05519030/)
* [Selene Báez Santamaría](https://selbaez.github.io/)
* [Piek Vossen](https://github.com/piekvossen)
